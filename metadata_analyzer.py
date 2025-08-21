#!/usr/bin/env python3
"""
Image Metadata Analyzer GUI
A comprehensive tool for extracting and analyzing image metadata with editing detection.

Author: Claude
Version: 1.0
Requirements: Python 3.6+, Pillow, pillow-heif (for HEIC support)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import os
import json
from datetime import datetime
import threading
from pathlib import Path
import io

# Import for HEIC support
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    HEIF_SUPPORT = False

class ImageMetadataAnalyzer:
    """Main application class for the Image Metadata Analyzer."""
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Image Metadata Analyzer v1.0")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Variables
        self.current_image_path = None
        self.metadata_dict = {}
        self.editing_indicators = []
        
        # Styling
        self.setup_styles()
        
        # Initialize GUI
        self.create_widgets()
        
        # Center window
        self.center_window()
    
    def setup_styles(self):
        """Configure custom styles for the application."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Success.TLabel', foreground='green')
        style.configure('Warning.TLabel', foreground='orange')
        style.configure('Error.TLabel', foreground='red')
    
    def center_window(self):
        """Center the application window on screen."""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Image Metadata Analyzer", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
        file_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(0, weight=1)
        
        # File path display and buttons
        path_frame = ttk.Frame(file_frame)
        path_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        path_frame.columnconfigure(0, weight=1)
        
        self.file_path_var = tk.StringVar(value="No file selected")
        self.file_path_label = ttk.Label(path_frame, textvariable=self.file_path_var,
                                        relief="sunken", padding="5")
        self.file_path_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Buttons frame
        buttons_frame = ttk.Frame(path_frame)
        buttons_frame.grid(row=0, column=1)
        
        self.upload_btn = ttk.Button(buttons_frame, text="Upload Image", 
                                    command=self.upload_image, width=12)
        self.upload_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.analyze_btn = ttk.Button(buttons_frame, text="Analyze", 
                                     command=self.analyze_metadata, width=12,
                                     state='disabled')
        self.analyze_btn.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(file_frame, variable=self.progress_var, 
                                          mode='determinate')
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Main content area with paned window
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Left panel - Image preview and summary
        left_frame = ttk.Frame(paned_window, width=350)
        paned_window.add(left_frame, weight=1)
        
        # Image preview
        preview_frame = ttk.LabelFrame(left_frame, text="Image Preview", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.image_label = ttk.Label(preview_frame, text="No image selected", 
                                    anchor="center", background="white", 
                                    relief="sunken")
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Analysis summary
        summary_frame = ttk.LabelFrame(left_frame, text="Analysis Summary", padding="10")
        summary_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.summary_text = scrolledtext.ScrolledText(summary_frame, height=8, 
                                                     width=40, wrap=tk.WORD)
        self.summary_text.pack(fill=tk.BOTH, expand=True)
        
        # Export button
        self.export_btn = ttk.Button(left_frame, text="Export Report", 
                                    command=self.export_report, state='disabled')
        self.export_btn.pack(fill=tk.X)
        
        # Right panel - Detailed metadata
        right_frame = ttk.Frame(paned_window)
        paned_window.add(right_frame, weight=2)
        
        metadata_frame = ttk.LabelFrame(right_frame, text="Detailed Metadata", padding="10")
        metadata_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview for metadata display
        columns = ('Property', 'Value', 'Description')
        self.metadata_tree = ttk.Treeview(metadata_frame, columns=columns, 
                                         show='tree headings', height=15)
        
        # Configure columns
        self.metadata_tree.column('#0', width=0, stretch=False)  # Hide tree column
        self.metadata_tree.column('Property', width=200, minwidth=150)
        self.metadata_tree.column('Value', width=250, minwidth=200)
        self.metadata_tree.column('Description', width=300, minwidth=250)
        
        # Configure headings
        for col in columns:
            self.metadata_tree.heading(col, text=col, anchor=tk.W)
        
        # Scrollbars for treeview
        v_scrollbar = ttk.Scrollbar(metadata_frame, orient=tk.VERTICAL, 
                                   command=self.metadata_tree.yview)
        h_scrollbar = ttk.Scrollbar(metadata_frame, orient=tk.HORIZONTAL, 
                                   command=self.metadata_tree.xview)
        self.metadata_tree.configure(yscrollcommand=v_scrollbar.set,
                                    xscrollcommand=h_scrollbar.set)
        
        # Grid treeview and scrollbars
        self.metadata_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        metadata_frame.columnconfigure(0, weight=1)
        metadata_frame.rowconfigure(0, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief="sunken", padding="2")
        status_bar.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Initialize summary text
        self.update_summary("No image loaded. Please upload an image to begin analysis.")
    
    def upload_image(self):
        """Handle image file upload."""
        filetypes = [
            ("All supported images", "*.jpg *.jpeg *.png *.tiff *.tif *.bmp *.gif"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("PNG files", "*.png"),
            ("TIFF files", "*.tiff *.tif"),
            ("BMP files", "*.bmp"),
            ("GIF files", "*.gif"),
        ]
        
        if HEIF_SUPPORT:
            filetypes.insert(1, ("HEIC/HEIF files", "*.heic *.heif"))
        
        filetypes.append(("All files", "*.*"))
        
        file_path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=filetypes
        )
        
        if file_path:
            self.current_image_path = file_path
            self.file_path_var.set(os.path.basename(file_path))
            self.analyze_btn.config(state='normal')
            self.status_var.set(f"Image loaded: {os.path.basename(file_path)}")
            
            # Load and display image preview
            self.load_image_preview()
            
            # Clear previous analysis
            self.clear_analysis()
    
    def load_image_preview(self):
        """Load and display image preview."""
        if not self.current_image_path:
            return
        
        try:
            # Open image and create thumbnail
            with Image.open(self.current_image_path) as img:
                # Calculate thumbnail size maintaining aspect ratio
                max_size = (300, 300)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Convert to PhotoImage for display
                photo = tk.PhotoImage(data=self.pil_to_photoimage(img))
                
                # Update label
                self.image_label.config(image=photo, text="")
                self.image_label.image = photo  # Keep a reference
                
        except Exception as e:
            self.image_label.config(image="", text=f"Preview unavailable\n{str(e)}")
            self.image_label.image = None
    
    def pil_to_photoimage(self, pil_image):
        """Convert PIL image to PhotoImage data."""
        buffer = io.BytesIO()
        pil_image.save(buffer, format='PNG')
        return buffer.getvalue()
    
    def analyze_metadata(self):
        """Analyze image metadata in a separate thread."""
        if not self.current_image_path:
            messagebox.showerror("Error", "No image selected")
            return
        
        # Disable analyze button and show progress
        self.analyze_btn.config(state='disabled')
        self.progress_var.set(0)
        self.status_var.set("Analyzing metadata...")
        
        # Run analysis in separate thread to keep GUI responsive
        thread = threading.Thread(target=self._analyze_metadata_thread)
        thread.daemon = True
        thread.start()
    
    def _analyze_metadata_thread(self):
        """Perform metadata analysis in background thread."""
        try:
            # Step 1: Extract basic metadata
            self.root.after(0, lambda: self.progress_var.set(20))
            metadata = self.extract_metadata()
            
            # Step 2: Analyze GPS data
            self.root.after(0, lambda: self.progress_var.set(40))
            gps_data = self.extract_gps_data(metadata)
            
            # Step 3: Check for editing indicators
            self.root.after(0, lambda: self.progress_var.set(60))
            editing_analysis = self.analyze_editing_indicators(metadata)
            
            # Step 4: Compile results
            self.root.after(0, lambda: self.progress_var.set(80))
            self.metadata_dict = {
                'basic_metadata': metadata,
                'gps_data': gps_data,
                'editing_analysis': editing_analysis,
                'file_info': self.get_file_info()
            }
            
            # Step 5: Update GUI
            self.root.after(0, lambda: self.progress_var.set(100))
            self.root.after(0, self.update_analysis_display)
            
        except Exception as e:
            self.root.after(0, lambda: self.handle_analysis_error(str(e)))
    
    def extract_metadata(self):
        """Extract metadata from the image using PIL."""
        metadata = {}
        
        try:
            with Image.open(self.current_image_path) as img:
                # Get basic image info
                metadata['Image Mode'] = img.mode
                metadata['Image Size'] = f"{img.width} x {img.height}"
                metadata['Image Format'] = img.format
                
                # Get EXIF data
                exifdata = img.getexif()
                
                if exifdata:
                    for tag_id in exifdata:
                        tag = TAGS.get(tag_id, tag_id)
                        data = exifdata.get(tag_id)
                        
                        # Handle special cases
                        if isinstance(data, bytes):
                            try:
                                data = data.decode('utf-8', errors='ignore')
                            except:
                                data = str(data)
                        
                        metadata[tag] = data
                
        except Exception as e:
            metadata['Error'] = f"Failed to extract metadata: {str(e)}"
        
        return metadata
    
    def extract_gps_data(self, metadata):
        """Extract and format GPS data from metadata."""
        gps_data = {}
        
        try:
            with Image.open(self.current_image_path) as img:
                exifdata = img.getexif()
                
                if exifdata and 'GPSInfo' in [TAGS.get(tag_id, tag_id) for tag_id in exifdata]:
                    gps_info = None
                    for tag_id in exifdata:
                        if TAGS.get(tag_id) == 'GPSInfo':
                            gps_info = exifdata[tag_id]
                            break
                    
                    if gps_info:
                        for key in gps_info:
                            name = GPSTAGS.get(key, key)
                            gps_data[name] = gps_info[key]
                        
                        # Convert coordinates to decimal degrees if available
                        if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
                            lat = self.convert_to_degrees(gps_data['GPSLatitude'])
                            lon = self.convert_to_degrees(gps_data['GPSLongitude'])
                            
                            if 'GPSLatitudeRef' in gps_data and gps_data['GPSLatitudeRef'] == 'S':
                                lat = -lat
                            if 'GPSLongitudeRef' in gps_data and gps_data['GPSLongitudeRef'] == 'W':
                                lon = -lon
                            
                            gps_data['Decimal Coordinates'] = f"{lat}, {lon}"
                
        except Exception as e:
            gps_data['Error'] = f"Failed to extract GPS data: {str(e)}"
        
        return gps_data
    
    def convert_to_degrees(self, value):
        """Convert GPS coordinates from DMS to decimal degrees."""
        if isinstance(value, (list, tuple)) and len(value) == 3:
            degrees, minutes, seconds = value
            return float(degrees) + float(minutes)/60 + float(seconds)/3600
        return float(value)
    
    def analyze_editing_indicators(self, metadata):
        """Analyze metadata for signs of image editing."""
        indicators = []
        likely_edited = False
        
        # Common editing software signatures
        editing_software = [
            'Adobe Photoshop', 'GIMP', 'Canva', 'Paint.NET', 'Corel',
            'Lightroom', 'Affinity', 'Sketch', 'Pixelmator', 'Snapseed'
        ]
        
        # Check software field
        software_field = metadata.get('Software', '')
        if software_field:
            for editor in editing_software:
                if editor.lower() in software_field.lower():
                    indicators.append(f"Editing software detected: {software_field}")
                    likely_edited = True
                    break
        
        # Check for missing typical camera metadata
        camera_fields = ['Make', 'Model', 'DateTime', 'ExifVersion']
        missing_fields = [field for field in camera_fields if field not in metadata]
        
        if len(missing_fields) > 2:
            indicators.append(f"Missing typical camera metadata: {', '.join(missing_fields)}")
        
        # Check for unusual aspect ratios (common in edited images)
        if 'Image Size' in metadata:
            try:
                size_parts = metadata['Image Size'].split(' x ')
                if len(size_parts) == 2:
                    width, height = int(size_parts[0]), int(size_parts[1])
                    aspect_ratio = width / height
                    
                    # Common camera ratios: 4:3, 3:2, 16:9
                    common_ratios = [4/3, 3/2, 16/9, 1/1]
                    min_diff = min([abs(aspect_ratio - ratio) for ratio in common_ratios])
                    
                    if min_diff > 0.1:  # Threshold for unusual ratio
                        indicators.append(f"Unusual aspect ratio: {aspect_ratio:.2f}")
            except:
                pass
        
        # Check for ColorSpace modifications
        if 'ColorSpace' in metadata and metadata['ColorSpace'] != 1:
            indicators.append("Non-standard color space detected")
        
        # Check creation vs modification dates
        creation_time = metadata.get('DateTime')
        modified_time = metadata.get('DateTimeDigitized')
        
        if creation_time and modified_time and creation_time != modified_time:
            indicators.append("Creation and modification timestamps differ")
        
        # Overall assessment
        if len(indicators) >= 2 or likely_edited:
            assessment = "Likely edited"
        elif len(indicators) == 1:
            assessment = "Possibly edited"
        else:
            assessment = "Likely original"
        
        return {
            'indicators': indicators,
            'assessment': assessment,
            'confidence': self.calculate_confidence(indicators, likely_edited)
        }
    
    def calculate_confidence(self, indicators, software_detected):
        """Calculate confidence level for editing assessment."""
        base_confidence = 30  # Base confidence
        
        if software_detected:
            base_confidence += 40
        
        base_confidence += len(indicators) * 15
        
        return min(base_confidence, 90)  # Cap at 90%
    
    def get_file_info(self):
        """Get basic file information."""
        if not self.current_image_path:
            return {}
        
        try:
            stat = os.stat(self.current_image_path)
            return {
                'File Name': os.path.basename(self.current_image_path),
                'File Size': f"{stat.st_size / 1024:.1f} KB",
                'Created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                'Modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'File Path': self.current_image_path
            }
        except Exception as e:
            return {'Error': f"Failed to get file info: {str(e)}"}
    
    def update_analysis_display(self):
        """Update GUI with analysis results."""
        try:
            # Clear previous results
            for item in self.metadata_tree.get_children():
                self.metadata_tree.delete(item)
            
            # Populate treeview with metadata
            if 'file_info' in self.metadata_dict:
                file_node = self.metadata_tree.insert('', 'end', text='File Information')
                for key, value in self.metadata_dict['file_info'].items():
                    self.metadata_tree.insert(file_node, 'end', 
                                            values=(key, str(value), 'Basic file properties'))
            
            if 'basic_metadata' in self.metadata_dict:
                basic_node = self.metadata_tree.insert('', 'end', text='Basic Metadata')
                for key, value in self.metadata_dict['basic_metadata'].items():
                    description = self.get_metadata_description(key)
                    self.metadata_tree.insert(basic_node, 'end', 
                                            values=(key, str(value), description))
            
            if 'gps_data' in self.metadata_dict and self.metadata_dict['gps_data']:
                gps_node = self.metadata_tree.insert('', 'end', text='GPS Information')
                for key, value in self.metadata_dict['gps_data'].items():
                    self.metadata_tree.insert(gps_node, 'end', 
                                            values=(key, str(value), 'GPS/Location data'))
            
            if 'editing_analysis' in self.metadata_dict:
                edit_node = self.metadata_tree.insert('', 'end', text='Editing Analysis')
                analysis = self.metadata_dict['editing_analysis']
                
                self.metadata_tree.insert(edit_node, 'end', 
                                        values=('Assessment', analysis['assessment'], 
                                               'Overall editing likelihood'))
                self.metadata_tree.insert(edit_node, 'end', 
                                        values=('Confidence', f"{analysis['confidence']}%", 
                                               'Analysis confidence level'))
                
                for i, indicator in enumerate(analysis['indicators']):
                    self.metadata_tree.insert(edit_node, 'end', 
                                            values=(f'Indicator {i+1}', indicator, 
                                                   'Potential editing sign'))
            
            # Expand all nodes
            for item in self.metadata_tree.get_children():
                self.metadata_tree.item(item, open=True)
            
            # Update summary
            self.update_summary_from_analysis()
            
            # Enable export button
            self.export_btn.config(state='normal')
            
            # Reset progress and status
            self.progress_var.set(0)
            self.status_var.set("Analysis complete")
            
        except Exception as e:
            self.handle_analysis_error(str(e))
        finally:
            # Re-enable analyze button
            self.analyze_btn.config(state='normal')
    
    def update_summary_from_analysis(self):
        """Update the analysis summary display."""
        if not self.metadata_dict:
            return
        
        summary_lines = []
        
        # File info summary
        if 'file_info' in self.metadata_dict:
            file_info = self.metadata_dict['file_info']
            summary_lines.append(f"📁 FILE: {file_info.get('File Name', 'Unknown')}")
            summary_lines.append(f"📏 SIZE: {file_info.get('File Size', 'Unknown')}")
            summary_lines.append("")
        
        # Camera info
        if 'basic_metadata' in self.metadata_dict:
            metadata = self.metadata_dict['basic_metadata']
            if 'Make' in metadata or 'Model' in metadata:
                camera = f"{metadata.get('Make', '')} {metadata.get('Model', '')}".strip()
                summary_lines.append(f"📷 CAMERA: {camera}")
            
            if 'DateTime' in metadata:
                summary_lines.append(f"📅 TAKEN: {metadata['DateTime']}")
            
            if 'Image Size' in metadata:
                summary_lines.append(f"🖼️ DIMENSIONS: {metadata['Image Size']}")
            summary_lines.append("")
        
        # GPS info
        if 'gps_data' in self.metadata_dict and self.metadata_dict['gps_data']:
            gps_data = self.metadata_dict['gps_data']
            if 'Decimal Coordinates' in gps_data:
                summary_lines.append(f"🗺️ LOCATION: {gps_data['Decimal Coordinates']}")
            else:
                summary_lines.append("🗺️ LOCATION: GPS data present")
            summary_lines.append("")
        
        # Editing analysis
        if 'editing_analysis' in self.metadata_dict:
            analysis = self.metadata_dict['editing_analysis']
            assessment = analysis['assessment']
            confidence = analysis['confidence']
            
            # Choose emoji based on assessment
            emoji = "✅" if assessment == "Likely original" else "⚠️" if assessment == "Possibly edited" else "❌"
            
            summary_lines.append(f"{emoji} EDITING STATUS:")
            summary_lines.append(f"   {assessment}")
            summary_lines.append(f"   Confidence: {confidence}%")
            summary_lines.append("")
            
            if analysis['indicators']:
                summary_lines.append("🔍 INDICATORS FOUND:")
                for indicator in analysis['indicators'][:3]:  # Show first 3
                    summary_lines.append(f"   • {indicator}")
                if len(analysis['indicators']) > 3:
                    summary_lines.append(f"   ... and {len(analysis['indicators']) - 3} more")
        
        self.update_summary('\n'.join(summary_lines))
    
    def get_metadata_description(self, key):
        """Get human-readable description for metadata fields."""
        descriptions = {
            'Make': 'Camera manufacturer',
            'Model': 'Camera model',
            'DateTime': 'Image capture date/time',
            'Software': 'Software used to process image',
            'Image Mode': 'Color mode (RGB, CMYK, etc.)',
            'Image Size': 'Width x Height in pixels',
            'Image Format': 'File format (JPEG, PNG, etc.)',
            'Orientation': 'Image orientation',
            'XResolution': 'Horizontal resolution (DPI)',
            'YResolution': 'Vertical resolution (DPI)',
            'Flash': 'Flash settings used',
            'ExposureTime': 'Shutter speed',
            'FNumber': 'Aperture f-stop',
            'ISO': 'ISO sensitivity',
            'FocalLength': 'Lens focal length',
            'ColorSpace': 'Color space information',
            'WhiteBalance': 'White balance setting'
        }
        return descriptions.get(key, 'Metadata field')
    
    def update_summary(self, text):
        """Update the summary text widget."""
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(1.0, text)
    
    def clear_analysis(self):
        """Clear all analysis results."""
        self.metadata_dict = {}
        self.update_summary("Ready to analyze. Click 'Analyze' to begin metadata extraction.")
        
        # Clear treeview
        for item in self.metadata_tree.get_children():
            self.metadata_tree.delete(item)
        
        # Disable export button
        self.export_btn.config(state='disabled')
    
    def handle_analysis_error(self, error_msg):
        """Handle errors during analysis."""
        self.progress_var.set(0)
        self.status_var.set(f"Analysis failed: {error_msg}")
        self.analyze_btn.config(state='normal')
        
        error_summary = f"❌ ANALYSIS ERROR:\n\n{error_msg}\n\nPlease ensure the selected file is a valid image."
        self.update_summary(error_summary)
        
        messagebox.showerror("Analysis Error", f"Failed to analyze image:\n{error_msg}")
    
    def export_report(self):
        """Export metadata report to text file."""
        if not self.metadata_dict:
            messagebox.showwarning("Warning", "No analysis data to export")
            return
        
        # Ask user for save location
        file_path = filedialog.asksaveasfilename(
            title="Save metadata report",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("IMAGE METADATA ANALYSIS REPORT\n")
                f.write("=" * 50 + "\n\n")
                
                # Write file information
                if 'file_info' in self.metadata_dict:
                    f.write("FILE INFORMATION:\n")
                    f.write("-" * 20 + "\n")
                    for key, value in self.metadata_dict['file_info'].items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n")
                
                # Write basic metadata
                if 'basic_metadata' in self.metadata_dict:
                    f.write("BASIC METADATA:\n")
                    f.write("-" * 20 + "\n")
                    for key, value in self.metadata_dict['basic_metadata'].items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n")
                
                # Write GPS data
                if 'gps_data' in self.metadata_dict and self.metadata_dict['gps_data']:
                    f.write("GPS INFORMATION:\n")
                    f.write("-" * 20 + "\n")
                    for key, value in self.metadata_dict['gps_data'].items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n")
                
                # Write editing analysis
                if 'editing_analysis' in self.metadata_dict:
                    analysis = self.metadata_dict['editing_analysis']
                    f.write("EDITING ANALYSIS:\n")
                    f.write("-" * 20 + "\n")
                    f.write(f"Assessment: {analysis['assessment']}\n")
                    f.write(f"Confidence: {analysis['confidence']}%\n\n")
                    
                    if analysis['indicators']:
                        f.write("Indicators found:\n")
                        for i, indicator in enumerate(analysis['indicators'], 1):
                            f.write(f"  {i}. {indicator}\n")
                    else:
                        f.write("No editing indicators found.\n")
                    f.write("\n")
                
                # Write generation info
                f.write(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("Generated by: Image Metadata Analyzer v1.0\n")
            
            messagebox.showinfo("Success", f"Report exported successfully to:\n{file_path}")
            self.status_var.set(f"Report exported: {os.path.basename(file_path)}")
            
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export report:\n{str(e)}")


def main():
    """Main function to run the application."""
    # Check for required dependencies
    missing_deps = []
    
    try:
        from PIL import Image, ExifTags
    except ImportError:
        missing_deps.append("Pillow")
    
    if missing_deps:
        print("Missing required dependencies:")
        for dep in missing_deps:
            print(f"  - {dep}")
        print("\nPlease install them using:")
        print("pip install " + " ".join(missing_deps))
        return
    
    # Create and run the application
    root = tk.Tk()
    app = ImageMetadataAnalyzer(root)
    
    # Handle window closing
    def on_closing():
        root.quit()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Application error: {e}")


if __name__ == "__main__":
    main()
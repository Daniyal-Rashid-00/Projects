export const metadata = {
  title: 'Daniyal Rashid - Lead Generation Specialist | Virtual Assistant | Cybersecurity Expert',
  description: 'Portfolio of Daniyal Rashid: Lead Generation, Virtual Assistant, and Cybersecurity expertise.',
};

import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}


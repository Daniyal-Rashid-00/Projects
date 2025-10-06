"use client";

import { useEffect } from "react";

export default function Page() {
  useEffect(() => {
    const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -100px 0px" };
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add("visible");
      });
    }, observerOptions);

    document
      .querySelectorAll(
        ".fade-in, .fade-in-left, .fade-in-right, .scale-in"
      )
      .forEach((el) => observer.observe(el));

    const sections = Array.from(document.querySelectorAll("section"));
    const navLinks = Array.from(document.querySelectorAll<HTMLAnchorElement>(".nav-links a"));
    const nav = document.querySelector("nav");
    const scrollTopBtn = document.querySelector(".scroll-top");

    const onScroll = () => {
      if (window.scrollY > 100) {
        nav?.classList.add("scrolled");
        scrollTopBtn?.classList.add("visible");
      } else {
        nav?.classList.remove("scrolled");
        scrollTopBtn?.classList.remove("visible");
      }

      let current = "";
      for (const section of sections) {
        const sectionTop = (section as HTMLElement).offsetTop;
        if (scrollY >= sectionTop - 200) current = section.getAttribute("id") || "";
      }
      navLinks.forEach((link) => {
        link.classList.remove("active");
        if (link.getAttribute("href")?.substring(1) === current) link.classList.add("active");
      });
    };
    window.addEventListener("scroll", onScroll);

    navLinks.forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        const targetId = link.getAttribute("href");
        if (!targetId) return;
        const targetSection = document.querySelector(targetId);
        if (targetSection) {
          const offsetTop = (targetSection as HTMLElement).offsetTop - 80;
          window.scrollTo({ top: offsetTop, behavior: "smooth" });
        }
      });
    });

    document
      .querySelectorAll(
        ".services-grid .service-card, .skills-grid .skill-item, .projects-grid .project-card"
      )
      .forEach((card, index) => {
        (card as HTMLElement).style.transitionDelay = `${index * 0.1}s`;
      });

    return () => {
      window.removeEventListener("scroll", onScroll);
      observer.disconnect();
    };
  }, []);

  return (
    <>
      <div className="bg-animation"></div>

      <nav>
        <div className="nav-container">
          <a href="#" className="logo">&lt;DR/&gt;</a>
          <ul className="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#certifications">Certifications</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>
      </nav>

      <section className="hero">
        <div className="hero-content">
          <div className="hero-subtitle">🎯 Lead Generation & 🔒 Cybersecurity Expert</div>
          <h1 className="hero-title">Daniyal Rashid</h1>
          <p className="hero-role">Lead Generation Specialist | Virtual Assistant | Cybersecurity Expert</p>
          <p className="hero-description">
            Transforming prospects into customers through data-driven outreach and secure automation. Specialized in lead generation, social media growth, and cybersecurity fundamentals.
          </p>
          <div className="hero-buttons">
            <a href="https://wa.me/923137840038" target="_blank" rel="noreferrer" className="btn btn-primary">Get In Touch</a>
            <a href="https://github.com/Daniyal-Rashid-00" target="_blank" rel="noreferrer" className="btn btn-secondary">View Projects</a>
          </div>
        </div>
      </section>

      <section id="about">
        <div className="section-header">
          <div className="section-tag">About Me</div>
          <h2 className="section-title">Turning Prospects Into Customers</h2>
        </div>
        <div className="about-content">
          <div className="about-text fade-in">
            <p>
              <strong>Lead Generation Specialist & Virtual Assistant</strong> — I design and run high-converting cold email and LinkedIn campaigns that turn prospects into customers. Recent outreach sequences achieved ~10–15% reply rates through targeted messaging and strategic follow-ups.
            </p>
            <p>
              As a BSIT student at the University of Punjab, I'm actively sharpening my cybersecurity fundamentals through CompTIA Security+ (SY0-601 / SY0-701) certification studies and hands-on practice on TryHackMe (20+ rooms completed, maintaining active learning streaks). This dual expertise allows me to prioritize secure, resilient lead pipelines and data handling practices in all client projects.
            </p>
            <p>
              I write clean, efficient "vibe" code—specializing in Python and n8n automations that scale outreach operations and streamline reporting workflows. My approach combines technical automation with strategic thinking to deliver measurable results: saved hours through workflow optimization, increased engagement through data-driven targeting, and protected client data through security-first implementation.
            </p>
            <p>
              <strong>Core Competencies:</strong> Cold Email/LinkedIn Outreach • Python & n8n Automation • Social Media Growth • Cybersecurity Fundamentals • Data Scraping & Analysis • Graphic Design • E-commerce Operations
            </p>
          </div>
        </div>

        <div className="stats-grid">
          <div className="stat-card scale-in">
            <div className="stat-number">10-15%</div>
            <div className="stat-label">Reply Rates</div>
          </div>
          <div className="stat-card scale-in">
            <div className="stat-number">50+</div>
            <div className="stat-label">Clients Served</div>
          </div>
          <div className="stat-card scale-in">
            <div className="stat-number">200%</div>
            <div className="stat-label">Revenue Growth</div>
          </div>
          <div className="stat-card scale-in">
            <div className="stat-number">95%</div>
            <div className="stat-label">Satisfaction Rate</div>
          </div>
        </div>
      </section>

      <section id="services" style={{ background: "var(--bg-secondary)" }}>
        <div className="section-header">
          <div className="section-tag">What I Offer</div>
          <h2 className="section-title">Services</h2>
          <p className="section-description">
            Specialized solutions to grow your business and secure your digital presence
          </p>
        </div>
        <div className="services-grid">
          <div className="service-card fade-in">
            <div className="service-icon">🎯</div>
            <h3>Lead Generation</h3>
            <p>
              Data-driven outreach campaigns via cold email and LinkedIn that achieve 10-15% reply rates. I build targeted prospect lists, craft compelling sequences, and optimize funnels to turn leads into paying customers.
            </p>
          </div>
          <div className="service-card fade-in">
            <div className="service-icon">📱</div>
            <h3>Social Media Services</h3>
            <p>
              Professional social media growth services including followers, subscribers, likes, views, and engagement boosting across all major platforms. Affordable packages tailored to help individuals and businesses amplify their online presence.
            </p>
          </div>
          <div className="service-card fade-in">
            <div className="service-icon">🔒</div>
            <h3>Cybersecurity Services</h3>
            <p>
              Security audits, vulnerability assessments, OSINT investigations, and secure automation implementation. Currently pursuing CompTIA Security+ certification to provide enterprise-grade security solutions.
            </p>
          </div>
          <div className="service-card fade-in">
            <div className="service-icon">📧</div>
            <h3>Email & DM Marketing</h3>
            <p>
              Strategic email campaigns and direct message outreach across multiple platforms. I create personalized messaging sequences, A/B test copy variations, and track engagement metrics to maximize conversions and ROI.
            </p>
          </div>
        </div>
      </section>

      <section id="skills">
        <div className="section-header">
          <div className="section-tag">Tech Stack</div>
          <h2 className="section-title">Skills & Tools</h2>
        </div>
        <div className="skills-grid">
          <div className="skill-item fade-in"><div className="skill-icon">🐍</div><h3>Python</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">🐉</div><h3>Kali Linux</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">🔒</div><h3>Cybersecurity</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">📊</div><h3>Data Scraping</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">🎯</div><h3>Lead Generation</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">🎨</div><h3>Graphic Design</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">💡</div><h3>Problem Solving</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">📝</div><h3>Notion</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">⚡</div><h3>Vibe Coding</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">🛡️</div><h3>Vulnerability Assessment</h3></div>
          <div className="skill-item fade-in"><div className="skill-icon">📧</div><h3>Email & DM Marketing</h3></div>
        </div>
      </section>

      <section id="certifications" style={{ background: "var(--bg-secondary)" }}>
        <div className="section-header">
          <div className="section-tag">Certifications</div>
          <h2 className="section-title">Professional Development</h2>
          <p className="section-description">Continuously learning and expanding my expertise</p>
        </div>
        <div className="certifications-grid">
          <div className="cert-card fade-in">
            <div className="cert-badge">🎓</div>
            <h3>CompTIA Security+</h3>
            <span className="cert-status">In Progress</span>
            <p className="cert-description">Currently pursuing CompTIA Security+ (SY0-601 & SY0-701) certification to strengthen cybersecurity fundamentals. Covering network security, compliance, operational security, threats and vulnerabilities, application security, and cryptography.</p>
          </div>
          <div className="cert-card fade-in">
            <div className="cert-badge">🔐</div>
            <h3>TryHackMe - Active Learner</h3>
            <span className="cert-status" style={{ background: "rgba(34, 197, 94, 0.1)", color: "#22c55e" }}>Active</span>
            <p className="cert-description">Rank: 435,786 | 20+ Rooms Completed | 24-Day Streak | 6 Badges Earned. Actively practicing penetration testing, Linux security, Windows exploitation (EternalBlue), and ethical hacking through hands-on challenges and CTF competitions.</p>
          </div>
        </div>
      </section>

      <section id="projects">
        <div className="section-header">
          <div className="section-tag">My Work</div>
          <h2 className="section-title">Featured Projects</h2>
          <p className="section-description">Cybersecurity assessments and custom development projects</p>
        </div>
        <div className="projects-grid">
          <div className="project-card fade-in-left">
            <div className="project-content">
              <span className="project-tag">Cybersecurity</span>
              <h3>Vulnerability Assessment Report - Banoqabil</h3>
              <p>Comprehensive vulnerability assessment conducted for Banoqabil platform. Identified security weaknesses, assessed risk levels, and provided detailed remediation strategies to strengthen the platform's security posture.</p>
              <div className="project-tech">
                <span className="tech-tag">Nmap</span>
                <span className="tech-tag">Burp Suite</span>
                <span className="tech-tag">OWASP</span>
                <span className="tech-tag">Security Analysis</span>
              </div>
              <a href="https://github.com/Daniyal-Rashid-00/BanoQabil-Vulnerability-Assessment-Report" target="_blank" rel="noreferrer" className="project-link">View Report →</a>
            </div>
          </div>

          <div className="project-card fade-in">
            <div className="project-content">
              <span className="project-tag">OSINT</span>
              <h3>OSINT Report - Bano Qabil</h3>
              <p>Open-Source Intelligence investigation report for banoqabil.pk. Utilized various OSINT tools and techniques to gather publicly available information, assess digital footprint, and provide security recommendations.</p>
              <div className="project-tech">
                <span className="tech-tag">OSINT Tools</span>
                <span className="tech-tag">Reconnaissance</span>
                <span className="tech-tag">Intelligence Gathering</span>
                <span className="tech-tag">Kali Linux</span>
              </div>
              <a href="https://github.com/Daniyal-Rashid-00/Banoqabil.pk-OSINT-Report" target="_blank" rel="noreferrer" className="project-link">View Report →</a>
            </div>
          </div>

          <div className="project-card fade-in-right">
            <div className="project-content">
              <span className="project-tag">Development</span>
              <h3>Dark Path</h3>
              <p>Self-hosted open-source communication software built with security and privacy in mind. Features end-to-end encryption, secure messaging, and complete control over your communication infrastructure.</p>
              <div className="project-tech">
                <span className="tech-tag">Python</span>
                <span className="tech-tag">Open Source</span>
                <span className="tech-tag">Encryption</span>
                <span className="tech-tag">Self-Hosted</span>
              </div>
              <a href="https://github.com/Daniyal-Rashid-00/Dark-Path--Messaging-App" target="_blank" rel="noreferrer" className="project-link">View on GitHub →</a>
            </div>
          </div>
        </div>
      </section>

      <section id="experience" style={{ background: "var(--bg-secondary)" }}>
        <div className="section-header">
          <div className="section-tag">Career Journey</div>
          <h2 className="section-title">Experience</h2>
        </div>
        <div className="timeline">
          <div className="timeline-item fade-in-left">
            <h3>Virtual Assistant</h3>
            <div className="timeline-company">Gift Craft & Hammad Gifts</div>
            <div className="timeline-meta">
              <span>📍 Remote / Gujranwala, Pakistan</span>
              <span>📅 Aug 2023 - Present</span>
            </div>
            <ul>
              <li>Streamlined e-commerce operations by optimizing workflows and implementing automation tools, resulting in a 30% reduction in order processing time and enhancing overall operational efficiency.</li>
              <li>Delivered exceptional customer support to over 1,000 clients annually through personalized engagement strategies, achieving a 95% satisfaction rate as reflected in customer feedback surveys.</li>
              <li>Designed over 150 visually appealing graphics for promotional campaigns that increased website traffic by 40%, leading to a significant revenue boost within three months.</li>
            </ul>
          </div>

          <div className="timeline-item fade-in-left">
            <h3>Founder & Social Media Marketing Strategist</h3>
            <div className="timeline-company">Everything SMM</div>
            <div className="timeline-meta">
              <span>📍 Hybrid / Gujranwala, Pakistan</span>
              <span>📅 Dec 2022 - Present</span>
            </div>
            <ul>
              <li>Established a full-service social media marketing agency that grew to serve over 50 clients within the first year, resulting in a 200% increase in monthly revenue and establishing a strong brand presence in the competitive digital landscape.</li>
              <li>Analyzed performance metrics for over 100 campaigns quarterly, refining approaches that resulted in an average ROI improvement of 35%, thereby enabling clients to achieve their digital marketing objectives consistently ahead of schedule.</li>
            </ul>
          </div>

          <div className="timeline-item fade-in-left">
            <h3>Freelance Graphic Designer | Digital Marketer</h3>
            <div className="timeline-company">Freelance</div>
            <div className="timeline-meta">
              <span>📍 Remote / Gujranwala, Punjab</span>
              <span>📅 Jan 2019 - Dec 2022</span>
            </div>
            <ul>
              <li>Developed innovative brand identities and marketing collateral for over 25 small businesses, resulting in a 50% increase in customer inquiries and a 35% boost in overall sales within the first quarter of implementation.</li>
              <li>Executed comprehensive social media campaigns across platforms, including Facebook and Instagram, leading to an impressive follower growth rate of 60% and engagement rates that surpassed industry benchmarks by 45%.</li>
            </ul>
          </div>
        </div>
      </section>

      <section id="education">
        <div className="section-header">
          <div className="section-tag">Academic Background</div>
          <h2 className="section-title">Education</h2>
        </div>
        <div className="education-grid">
          <div className="education-card fade-in">
            <h3>University of the Punjab</h3>
            <div className="education-degree">BSIT (Bachelor of Science in Information Technology)</div>
            <div className="education-meta">📍 Punjab, Pakistan | 🎓 2025 - Present</div>
          </div>
          <div className="education-card fade-in">
            <h3>Post Graduate Govt College Gujranwala</h3>
            <div className="education-degree">ICS (Intermediate in Computer Science)</div>
            <div className="education-meta">📍 Gujranwala, Punjab | 🎓 Expected: May 2025</div>
          </div>
          <div className="education-card fade-in">
            <h3>The Gujranwala Public High School</h3>
            <div className="education-degree">Matriculation in Computer Science</div>
            <div className="education-meta">📍 Gujranwala, Punjab | 🎓 Feb 2023</div>
          </div>
        </div>
      </section>

      <section id="contact" style={{ background: "var(--bg-secondary)" }}>
        <div className="section-header">
          <div className="section-tag">Get In Touch</div>
          <h2 className="section-title">Let's Work Together</h2>
          <p className="section-description">Ready to scale your lead generation, grow your social presence, or secure your systems? Let's connect!</p>
        </div>
        <div className="contact-content fade-in">
          <div className="contact-info">
            <div className="contact-item">
              <span>📧</span>
              <a href="mailto:the.daniyal.rashid@gmail.com">the.daniyal.rashid@gmail.com</a>
            </div>
            <div className="contact-item">
              <span>📞</span>
              <a href="tel:+923137840038">+92-313-7840038</a>
            </div>
            <div className="contact-item">
              <span>📍</span>
              <span>Gujranwala, Punjab, Pakistan</span>
            </div>
          </div>
          <div className="social-links">
            <a href="https://github.com/Daniyal-Rashid-00" target="_blank" rel="noreferrer" className="social-link" title="GitHub">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            </a>
            <a href="https://www.linkedin.com/in/the-daniyal-rashid/" target="_blank" rel="noreferrer" className="social-link" title="LinkedIn">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
            <a href="https://discord.com/users/daniyal_rashid" target="_blank" rel="noreferrer" className="social-link" title="Discord: daniyal_rashid">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12 .098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
            </a>
            <a href="https://tryhackme.com/p/Daniyal01" target="_blank" rel="noreferrer" className="social-link" title="TryHackMe">
              <span style={{ fontSize: '1.1rem', fontWeight: 700 }}>THM</span>
            </a>
          </div>
        </div>
      </section>

      <footer>
        <p>© 2025 Daniyal Rashid. All rights reserved.</p>
        <p style={{ marginTop: '0.5rem', fontSize: '0.9rem' }}>
          🌐 Available for remote opportunities | 💬 Fluent in English, Urdu, Punjabi & Hindi
        </p>
      </footer>

      <div className="scroll-top" onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}>↑</div>
    </>
  );
}



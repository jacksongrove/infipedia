# 🌐 Infipedia
## Reviving the Joy of Browsing the Internet

Infipedia is an infinite, Wikipedia-inspired browsing experience powered by AI. Inspired by the feeling of raw discovery brought by browsing the early internet, Infipedia eliminates ads, clickbait, SEO spam, and distractions to focus on genuine exploration and knowledge discovery. Built using **Streamlit** for an intuitive user interface and **Groq** for lightning-fast content delivery, this project aims to bring back the magic of OG online exploration.

<video src="https://github.com/user-attachments/assets/ff358e1b-0845-4029-9761-d26a17564ddd" controls="controls" style="max-width: 100%;">
    Your browser does not support the video tag.
</video>

---
## About

Infipedia reimagines the joy of discovery that once defined browsing the internet—before ads, clickbait and SEO spam took over. Inspired by **Wikipedia**’s simplicity and intuitive exploration model—minimal distractions, informative content, and links to countless rabbithole topics—Infipedia provides the same ease of browsing but uses AI to fill in gaps where traditional encyclopedias or single sites fall short. By tapping into the entire internet for context, it dynamically generates new topic pages, ensuring there are no dead ends, no matter how obscure or deep your search.

Under the hood, a series of AI agents powered by Groq enables near-instant content generation and delivery, providing a lightning-fast experience so users can quickly switch between topics. Meanwhile, Streamlit supports the simple and intuitive interface, making it easy to search, browse, and dive into the many rabbitholes of knowledge that Infipedia has to offer. The result is an infinitely expanding, distraction-free world of information—taking the best from the Wikipedia browsing experience, but supercharged by AI.

Infipedia is available at https://infipedia.jacksongrove.me

---

## Getting Started

#### **1. Clone the repo**
   ```
   git clone https://github.com/jacksongrove/infipedia.git
   ```

#### **2. Set up environment variables**

   Create `.env` file from the template
   ```
   cp .env.template .env
   ```
   Within `.env`, replace `GROQ_API_KEY=gsk_your_actual_api_key_here` with your actual Groq API key
   
#### **3. Install docker**
  ```
  curl -fsSL https://get.docker.com | sh
  ```
  Allow Docker commands to be run without `sudo`
  ```
  sudo usermod -aG docker $USER
  ```
  Log out and back in to your shell for the changes to take effect

  NOTE: Alternatively you can install Docker Desktop

#### **4. Build the docker image**
  ```
  docker build -t <image-name> .
  ```

#### **5. Run the image using the `.env` file**
  ```
  docker run -d -p 8501:8501 --env-file .env <image-name>
  ```

#### **6. Access the app through ``http://localhost:8501`` on your local machine**

---

## Contributions Welcome!

Here’s how you can help...

If you find a bug or have suggestions for improvement:
   1.	Open an issue on GitHub.
   2.	Provide a clear description of the problem or suggestion.

Contributing Code
   1.	Fork the repository.
   2.	Create a new branch for your feature or bug fix.
   3. Open a Pull Request.

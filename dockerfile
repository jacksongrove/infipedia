# Use the official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install streamlit

# Streamlit-specific config (optional)
RUN mkdir -p ~/.streamlit
RUN echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
enableXsrfProtection=false\n\
port = 8501\n\
" > ~/.streamlit/config.toml

# Expose the Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--client.showSidebarNavigation", "False", "--server.address", "0.0.0.0"]
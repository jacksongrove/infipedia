# Use the official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
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

# Create the /var/log directory and touch the cron log file
RUN mkdir -p /var/log && touch /var/log/cron.log

# Add the cron job to delete pages after 10 minutes
RUN echo "PATH=/usr/local/bin:/usr/bin:/bin" > /etc/environment && \
    echo "*/10 * * * * /usr/local/bin/python3 /app/delete_old_pages.py >> /var/log/cron.log 2>&1" > /etc/cron.d/delete_old_files

# Set permissions for the cron job file and install it
RUN chmod 0644 /etc/cron.d/delete_old_files && crontab /etc/cron.d/delete_old_files

# Start the cron service alongside Streamlit
CMD cron && streamlit run app.py --client.showSidebarNavigation False --server.address 0.0.0.0
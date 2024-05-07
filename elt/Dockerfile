FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ELT script 
COPY api-snowflake-script.py .

# Set the default command to run the ELT script
CMD ["python", "api-snowflake-script.py"]

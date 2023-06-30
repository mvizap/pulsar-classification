# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY main.py .

#Copy the notebook
COPY My_notebook.ipynb.ipynb .
CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "/home/jovyan/work/my_notebook.ipynb", "--ExecutePreprocessor.timeout=-1"]

# Run the Python script when the conainer launches
ENTRYPOINT ["python", "main.py"]
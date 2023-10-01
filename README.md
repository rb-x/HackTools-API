<center><h1> HackTools server</h1></center>

## Description


This project serves as a compact web server, offering a REST API that leverages the power of Python's offensive dumping libraries to decrypt Windows credentials. It's designed to work in conjunction with the [Hacktools](https://github.com/LasCC/HackTools) project.



## 🚀 Features

- SAM file decryption.
- LSASS dump decryption (TODO).
- NTDS file decryption (TODO).


## 🛠️ Installation


There are two convenient methods available for installing the server: you can opt for a manual installation or use Docker for a streamlined setup process.


### Manual installation

```bash
pip install pipenv # Install pipenv if you don't have it
pipenv shell # Create a virtual environment
pipenv install # Install dependencies
chmod +x ./run.py # Make the script executable
./run.py # Run the server at localhost:8001
```

### Docker

```bash
docker build -t hacktools-backend . # Build the image
docker run -d -p 8001:8001 hacktools-backend # Run the container
```

### 📚 API Endpoints

- `/`: Root endpoint that returns a welcome message.
- `/ping`: Endpoint to check if the server is up.
- `auth_check`: Endpoint to check if the API key is valid.
- `/docs`: Endpoint for the Swagger UI (only if **HTOOLS_SERVER_DEV** environment variable is set).

---
- `/decrypt/sam` (POST): Endpoint to decrypt a SAM file with SYSTEM Hive.

---
**TODO:**
- `/decrypt/ntds` (POST): Endpoint to decrypt a NTDS file with SYSTEM Hive (TODO).
- `/decrypt/lsass` (POST): Endpoint to decrypt a LSASS dump (TODO).


## 🚀 Usage

Link the frontend to the backend by setting the server URL and the API key in the frontend settings of Hacktools.


## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## 📜 License

This project is licensed under the GPLv3 License - see the LICENSE file for details.

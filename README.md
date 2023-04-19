# visitors-observer

Collect and processed incoming events with face on photo 


# Autodocumentation swagger:

ip_address:port/docs
ip_address:port/redoc


Install for local development:

    ```sh
    git clone https://github.com/yastcher/visitors-observer.git
    ```

Run or install virtual environments:

    ```sh
    poetry env
    ```

Install requirements:

    ```sh
    poetry install
    ```

Start app:
    ```sh
    uvicorn main:app --host 127.0.0.1 --port 5555
    ```

Autodocumentation (swagger):
    ```sh
    http://127.0.0.1:5555/docs
    http://127.0.0.1:5555/redoc
    ```

Run tests (pytest):
    ```sh
    pytest
    ```

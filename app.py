if __name__ == '__main__':
    import time 
    try:
        from src.FreeGPT4_Server import app
        app.run("0.0.0.0", port=8080, debug=False)
    except:
        print("lanch error")
    time.sleep(1800)
    #python3 ./src/FreeGPT4_Server.py

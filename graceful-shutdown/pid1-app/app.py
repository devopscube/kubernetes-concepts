from flask import Flask
import signal
import time
import sys

app = Flask(__name__)
is_shutting_down = False

def handle_sigterm(signum, frame):
    global is_shutting_down
    print("\n[SHUTDOWN] SIGTERM signal received.")
    is_shutting_down = True
    print("[SHUTDOWN] Finishing remaining tasks before exit...")
    time.sleep(1)
    print("[SHUTDOWN] Saving in-progress orders to database...")
    time.sleep(1)
    print("[SHUTDOWN] Notifying other services that shutdown is happening...")
    time.sleep(1)
    print("[SHUTDOWN] Cleanup complete. Shutting down gracefully.")
    
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

@app.route("/work")
def do_work():
    if is_shutting_down:
        print("[WORK] Rejected request: shutting down.")
        return "Server is shutting down. Try again later.\n", 503

    print("[WORK] New order processing started...")
    time.sleep(3)
    print("[WORK] Validating order data...")
    time.sleep(2)
    print("[WORK] Writing order to database...")
    time.sleep(2)
    print("[WORK] Order processed successfully.")
    return "Order processed successfully!\n"

@app.route("/")
def home():
    return "Welcome to the Order Processing App\n"

if __name__ == "__main__":
    print("[APP] Starting Flask app...")
    app.run(host="0.0.0.0", port=5000)

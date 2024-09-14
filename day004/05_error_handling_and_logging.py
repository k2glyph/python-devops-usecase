import logging

# configure logging
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_task():
    try:
        logging.info("Task started")
        # simulating a task
        result= f110/0 # This will return a ZeroDivisionError
        logging.info(f"Task result{result}")
    except ZeroDivisionError as e:
        logging.error(f"An error occurred: {e}")
    except Exception as e:
        logging.error(f'Unexcepted error occur: {e}')

if __name__ == "__main__":
    perform_task()

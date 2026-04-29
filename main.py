from agent import run_agent

def main():
    try:
        report = run_agent()
        with open("daily_report.txt", "w") as f:
            f.write(report)
        print("Success! Report saved to daily_report.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
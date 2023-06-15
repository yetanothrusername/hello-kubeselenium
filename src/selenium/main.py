import subprocess

def main():
    test_type = input("Enter the type of test (chrome/firefox/ie): ")

    if test_type == "chrome":
        subprocess.run(["python", "test_chrome.py"])
    elif test_type == "firefox":
        subprocess.run(["python", "test_firefox.py"])
    elif test_type == "ie":
        subprocess.run(["python", "test_ie.py"])
    else:
        print("Invalid test type specified.")

if __name__ == "__main__":
    main()

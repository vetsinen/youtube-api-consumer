import json

def main():

    with open('vitaliy.gusak24@gmail.com.json', 'r') as f:
        data = json.load(f)

    # Output: {'name': 'Bob', 'languages': ['English', 'French']}
    print(data)


if __name__ == '__main__':
    main()
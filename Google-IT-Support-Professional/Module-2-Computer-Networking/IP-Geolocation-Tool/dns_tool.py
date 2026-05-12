import socket
import requests

def get_ip_info(target_domain):
    print("-" * 50)
    print(f"Аналіз для: {target_domain}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(target_domain)
        print(f"IP Address: {target_ip}")
        response = requests.get(f"http://ip-api.com/json/{target_ip}")
        data = response.json()

        if data["status"] == "success":
            print(f"Country:    {data.get('country')}")
            print(f"Region/City: {data.get('regionName')} / {data.get('city')}")
            print(f"ISP:         {data.get('isp')}")
            print(f"Latitude:    {data.get('lat')}")
            print(f"Longitude:   {data.get('lon')}")
        else:
            print("[!] Не вдалося отримати геолокацію.")

    except socket.gaierror:
        print("[!] Помилка: Не вдалося знайти IP для цього домену.")
    except Exception as e:
        print(f"[!] Виникла помилка: {e}")

if __name__ == "__main__":
    domain = input("Введіть домен (наприклад, google.com): ")
    get_ip_info(domain)
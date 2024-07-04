import requests
from bs4 import BeautifulSoup  # for basic HTML parsing

def footprint_website(url):
  """
  This function passively gathers information from a website using its URL.

  Args:
      url (str): The URL of the website to footprint.

  Returns:
      dict: A dictionary containing information found on the website.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information from the website (replace with your desired data points)
    title = soup.title.string.strip()
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description:
      description = meta_description['content'].strip()
    else:
      description = "No description found"

    # Return a dictionary with the extracted information
    return {
      "title": title,
      "description": description,
    }

  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return {}

if __name__ == "__main__":
  # Replace with the target website URL (ensure it's publicly accessible)
  target_url = input("Enter the Website name")
  website_info = footprint_website(target_url)

  if website_info:
    print(f"  Title: {website_info['title']}")
    print(f"  Description: {website_info['description']}")
  else:
    print("Website information could not be retrieved.")

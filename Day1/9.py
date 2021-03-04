from bs4 import BeautifulSoup
from IPython import embed
import re

def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>

            <script>
                var hello="yoh";
                alert(hello);
            </script>

            </body>
        </html>
    """

def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, "html.parser")

    scraped = soup.find("script") #eric's solution
    pattern = re.compile("var hello=\"(.*?)\";") #make a patter to get the string
    print(pattern.findall(scraped.string)[0]) #get all the string with the pattern above

if __name__ == "__main__":
    main()
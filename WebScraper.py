import pandas as pd
import Files as f

class Scraper:

    @staticmethod
    def scrape(sheet_url):
        try:
            # Correct the URL format for CSV export
            csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
            df = pd.read_csv(csv_export_url)
            return df
        except pd.errors.ParserError as e:
            print(f"Error parsing CSV: {e}")
            return pd.DataFrame()  # Return an empty DataFrame or handle as needed
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame or handle as needed

    @staticmethod
    def convert_to_string(df):
        return df.to_string(index=False)  # `index=False` omits the row numbers
    
    def scrapeToFile(data,name,extension):
        f.FileWriter.writeToFile(content=data, name=name, extension=extension)

if __name__ == '__main__':
    # Correct URLs for CSV export
    url1 = "https://docs.google.com/spreadsheets/d/12SYPRGPIVJ2-bY01ksF4aqdinZDbyD-LN2ipeB5i6T0/export?format=csv&gid=0"
    url2 = "https://docs.google.com/spreadsheets/d/140MawDp6uzxSR6lgICO4USXKe7QektrSHRstomDdsVs/export?format=csv&gid=0"
    
    # Scrape and write data to files
    #content1 = Scraper.convert_to_string(Scraper.scrape(url1))
    #f.FileWriter.writeToFile(content=content1, name='Data', extension='.txt')
    Scraper.scrapeToFile(data=Scraper.convert_to_string(Scraper.scrape(url1)),name='Data',extension='.txt')
    Scraper.scrapeToFile(data=Scraper.convert_to_string(Scraper.scrape(url2)),name='Data2',extension='.txt')
    
    #content2 = Scraper.convert_to_string(Scraper.scrape(url2))
    #f.FileWriter.writeToFile(content=content2, name='Data2', extension='.txt')

import pandas as pd
import Files as f


class Scraper:

    def scrape():
        sheet_url = "https://docs.google.com/spreadsheets/d/12SYPRGPIVJ2-bY01ksF4aqdinZDbyD-LN2ipeB5i6T0/edit#gid=0"
        csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
        df = pd.read_csv(csv_export_url)
        return df
    def convert_to_string(df):
        df_string = df.to_string(index=False)  # `index=False` omits the row numbers
        return df_string


if __name__ == '__main__':
    f.FileWriter.writeToFile(content=Scraper.convert_to_string(Scraper.scrape()),name='Data',extension='.txt')
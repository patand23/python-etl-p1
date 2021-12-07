import csv
import sql
from pgsql import query

def all():
    ats()
    hg()
    pct()
    td()
    tg()
    tgr()
    tgs()
    tpm()
    wrc()

def ats():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            row.pop()
            #print(row)
            query(sql.insert_ats, row)

def hg():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_hg, row)

def pct():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_pct, row)

def td():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_td, row)

def tg():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_tg, row)

def tgr():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_tgr, row)

def tgs():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_tgs, row)

def tpm():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            query(sql.insert_tpm, row)

def wrc():
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv', newline='', encoding="utf-8-sig") as csvf:
        reader = csv.reader(csvf, delimiter=',')
        next(reader)
        for row in reader:
            row.pop()
            #print(row)
            query(sql.insert_wrc, row)

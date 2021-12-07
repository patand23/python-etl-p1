
create_schema = ('''
  CREATE SCHEMA IF NOT EXISTS petl1;
''')

insert_ats = ('''
  INSERT INTO petl1.Annual_Ticket_Sales
  values (%s,%s,%s,%s,%s);
''')

insert_hg = ('''
  INSERT INTO petl1.Highest_Grossers
  values (%s,%s,%s,%s,%s,%s,%s,%s);
''')

insert_pct = ('''
  INSERT INTO petl1.Popular_Creative_Types
  values (%s,%s,%s,%s,%s,%s);
''')

insert_td = ('''
  INSERT INTO petl1.Top_Distributors
  values (%s,%s,%s,%s,%s,%s);
''')

insert_tg = ('''
  INSERT INTO petl1.Top_Genres
  values (%s,%s,%s,%s,%s,%s);
''')

insert_tgr = ('''
  INSERT INTO petl1.Top_Grossing_Ratings
  values (%s,%s,%s,%s,%s,%s);
''')

insert_tgs = ('''
  INSERT INTO petl1.Top_Grossing_Sources
  values (%s,%s,%s,%s,%s,%s);
''')

insert_tpm = ('''
  INSERT INTO petl1.Top_Production_Methods
  values (%s,%s,%s,%s,%s,%s);
''')

insert_wrc = ('''
  INSERT INTO petl1.Wide_Releases_Count
  values (%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')



create_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.Annual_Ticket_Sales(
    year text,
    tickets_sold text,
    total_box_office text,
    total_inflation_adjusted_box_office text,
    average_ticket_price text);

  CREATE TABLE IF NOT EXISTS petl1.Highest_Grossers(
    year text,
    movie text,
    genre text,
    mpaa_rating text,
    distributor text,
    total_for_year text,
    total_in_2019_dollars text,
    tickets_sold text);

  CREATE TABLE IF NOT EXISTS petl1.Popular_Creative_Types(
    rank text,
    creative_types text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Top_Distributors(
    rank text,
    distributors text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Top_Genres(
    rank text,
    genres text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Top_Grossing_Ratings(
    rank text,
    mpaa_rating text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Top_Grossing_Sources(
    rank text,
    sources text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Top_Production_Methods(
    rank text,
    production_methods text,
    movies text,
    total_gross text,
    average_gross text,
    market_share text);

  CREATE TABLE IF NOT EXISTS petl1.Wide_Releases_Count(
    year text,
    warner_bros text,
    walt_disney text,
    twentieth_century_fox text,
    paramount_pictures text,
    sony_pictures text,
    universal text,
    total_major_6 text,
    total_other_studios text);
''')
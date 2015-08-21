--------------------------------------------------------------------------------
-- Table: stock_symbol
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS stock_symbol;

CREATE TABLE stock_symbol
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stock_name text,
  isin_code text,
  listing_date date,
  market_category text,
  industry_category text,
  cfi_code text,
  CONSTRAINT stock_symbol_unique_key UNIQUE (release_date, stock_symbol)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE stock_symbol
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: balance_sheet
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS balance_sheet;

CREATE TABLE balance_sheet
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT balance_sheet_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE balance_sheet
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: income_statement
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS income_statement;

CREATE TABLE income_statement
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT income_statement_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE income_statement
  OWNER TO stockcat;  
  
--------------------------------------------------------------------------------
-- Table: cash_flow
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS cash_flow;

CREATE TABLE cash_flow
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT cash_flow_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE cash_flow
  OWNER TO stockcat; 

--------------------------------------------------------------------------------
-- Table: operating_revenue
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS operating_revenue;

CREATE TABLE operating_revenue
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT operating_revenue_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE operating_revenue
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: capital_increase_history
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS capital_increase_history;

CREATE TABLE capital_increase_history
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT capital_increase_history_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE capital_increase_history
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: dividend_policy
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS dividend_policy;

CREATE TABLE dividend_policy
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT dividend_policy_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dividend_policy
  OWNER TO stockcat;  

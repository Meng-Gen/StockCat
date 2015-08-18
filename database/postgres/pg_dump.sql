--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: capital_increase_history; Type: TABLE; Schema: public; Owner: stockcat; Tablespace: 
--

CREATE TABLE capital_increase_history (
    creation_dt timestamp without time zone DEFAULT now(),
    release_date date NOT NULL,
    stock_symbol text NOT NULL,
    stmt_date date NOT NULL,
    account text NOT NULL,
    account_order smallint,
    value double precision
);


ALTER TABLE capital_increase_history OWNER TO stockcat;

--
-- Name: dividend_policy; Type: TABLE; Schema: public; Owner: stockcat; Tablespace: 
--

CREATE TABLE dividend_policy (
    creation_dt timestamp without time zone DEFAULT now(),
    release_date date NOT NULL,
    stock_symbol text NOT NULL,
    stmt_date date NOT NULL,
    account text NOT NULL,
    account_order smallint,
    value double precision
);


ALTER TABLE dividend_policy OWNER TO stockcat;

--
-- Name: operating_revenue; Type: TABLE; Schema: public; Owner: stockcat; Tablespace: 
--

CREATE TABLE operating_revenue (
    creation_dt timestamp without time zone DEFAULT now(),
    release_date date NOT NULL,
    stock_symbol text NOT NULL,
    stmt_date date NOT NULL,
    account text NOT NULL,
    account_order smallint,
    value double precision
);


ALTER TABLE operating_revenue OWNER TO stockcat;

--
-- Name: stock_symbol; Type: TABLE; Schema: public; Owner: stockcat; Tablespace: 
--

CREATE TABLE stock_symbol (
    creation_dt timestamp without time zone DEFAULT now(),
    release_date date NOT NULL,
    stock_symbol text NOT NULL,
    stock_name text,
    isin_code text,
    listing_date date,
    market_category text,
    industry_category text,
    cfi_code text
);


ALTER TABLE stock_symbol OWNER TO stockcat;

--
-- Name: public; Type: ACL; Schema: -; Owner: stockcat
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM stockcat;
GRANT ALL ON SCHEMA public TO stockcat;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


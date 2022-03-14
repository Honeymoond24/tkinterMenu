--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0
-- Dumped by pg_dump version 14.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dish; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dish (
    id bigint NOT NULL,
    name text NOT NULL,
    description text NOT NULL,
    picture text,
    weight double precision NOT NULL,
    pfc double precision NOT NULL,
    type text
);


ALTER TABLE public.dish OWNER TO postgres;

--
-- Name: dish_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dish_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dish_id_seq OWNER TO postgres;

--
-- Name: dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dish_id_seq OWNED BY public.dish.id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    id bigint NOT NULL,
    dish_id bigint NOT NULL,
    date_ordered timestamp without time zone NOT NULL,
    cost double precision NOT NULL
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_id_seq OWNER TO postgres;

--
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- Name: products_dish; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products_dish (
    id bigint NOT NULL,
    product_id bigint NOT NULL,
    dish_id bigint NOT NULL,
    count integer NOT NULL
);


ALTER TABLE public.products_dish OWNER TO postgres;

--
-- Name: products_dish_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_dish_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_dish_id_seq OWNER TO postgres;

--
-- Name: products_dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_dish_id_seq OWNED BY public.products_dish.id;


--
-- Name: products_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products_item (
    id bigint NOT NULL,
    name text NOT NULL,
    count integer NOT NULL,
    units text NOT NULL,
    type text
);


ALTER TABLE public.products_item OWNER TO postgres;

--
-- Name: products_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_item_id_seq OWNER TO postgres;

--
-- Name: products_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_item_id_seq OWNED BY public.products_item.id;


--
-- Name: dish id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dish ALTER COLUMN id SET DEFAULT nextval('public.dish_id_seq'::regclass);


--
-- Name: order id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- Name: products_dish id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_dish ALTER COLUMN id SET DEFAULT nextval('public.products_dish_id_seq'::regclass);


--
-- Name: products_item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_item ALTER COLUMN id SET DEFAULT nextval('public.products_item_id_seq'::regclass);


--
-- Data for Name: dish; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dish (id, name, description, picture, weight, pfc, type) FROM stdin;
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."order" (id, dish_id, date_ordered, cost) FROM stdin;
\.


--
-- Data for Name: products_dish; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_dish (id, product_id, dish_id, count) FROM stdin;
\.


--
-- Data for Name: products_item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_item (id, name, count, units, type) FROM stdin;
\.


--
-- Name: dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dish_id_seq', 1, false);


--
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_id_seq', 1, false);


--
-- Name: products_dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_dish_id_seq', 1, false);


--
-- Name: products_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_item_id_seq', 1, false);


--
-- Name: dish dish_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_pk PRIMARY KEY (id);


--
-- Name: order order_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pk PRIMARY KEY (id);


--
-- Name: products_dish products_dish_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_dish
    ADD CONSTRAINT products_dish_pk PRIMARY KEY (id);


--
-- Name: products_item products_item_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_item
    ADD CONSTRAINT products_item_pk PRIMARY KEY (id);


--
-- Name: order order_dish_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_dish_id_fk FOREIGN KEY (dish_id) REFERENCES public.dish(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: products_dish products_dish_dish_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_dish
    ADD CONSTRAINT products_dish_dish_id_fk FOREIGN KEY (dish_id) REFERENCES public.dish(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: products_dish products_dish_products_item_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_dish
    ADD CONSTRAINT products_dish_products_item_id_fk FOREIGN KEY (product_id) REFERENCES public.products_item(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--


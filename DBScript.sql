-- address 

-- Table: public.address

-- DROP TABLE IF EXISTS public.address;

CREATE TABLE IF NOT EXISTS public.address
(
    addressid integer NOT NULL DEFAULT nextval('address_id_seq'::regclass),
    typeofaddress character varying(120) COLLATE pg_catalog."default" NOT NULL,
    address_desc character varying(120) COLLATE pg_catalog."default" NOT NULL,
    createddate time without time zone NOT NULL,
    updateddate time without time zone NOT NULL,
    userid integer,
    CONSTRAINT address_pkey PRIMARY KEY (addressid, typeofaddress, address_desc, createddate, updateddate),
    CONSTRAINT userid_fkey FOREIGN KEY (userid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.address
    OWNER to postgres;
-- Table: public.canteen

-- DROP TABLE IF EXISTS public.canteen;

CREATE TABLE IF NOT EXISTS public.canteen
(
    canteenid integer NOT NULL DEFAULT nextval('canteen_id_seq'::regclass),
    location character varying(120) COLLATE pg_catalog."default" NOT NULL,
    canteenname character varying(120) COLLATE pg_catalog."default" NOT NULL,
    canteenowner character varying(120) COLLATE pg_catalog."default" NOT NULL,
    canteenstatus character varying(120) COLLATE pg_catalog."default" NOT NULL,
    createddate time without time zone,
    updateddate time without time zone,
    CONSTRAINT canteen_pkey PRIMARY KEY (canteenid),
    CONSTRAINT canteenowner_username_fkey FOREIGN KEY (canteenowner)
        REFERENCES public.users (username) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.canteen
    OWNER to postgres;

COMMENT ON CONSTRAINT canteenowner_username_fkey ON public.canteen
    IS 'canteen owner should be defined as username in user table';

-- Table: public.cart

-- DROP TABLE IF EXISTS public.cart;

CREATE TABLE IF NOT EXISTS public.cart
(
    cartid integer NOT NULL DEFAULT nextval('cart_id_seq'::regclass),
    orderid integer NOT NULL,
    cartstatus character varying(50) COLLATE pg_catalog."default" NOT NULL,
    cartprice integer NOT NULL,
    cartusername character varying(120) COLLATE pg_catalog."default" NOT NULL,
    createddate time without time zone,
    updateddate time without time zone,
    cartuserid integer,
    CONSTRAINT cart_pkey PRIMARY KEY (cartid),
    CONSTRAINT cart_order_fkey FOREIGN KEY (orderid)
        REFERENCES public."order" (orderid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cart_user_fkey FOREIGN KEY (cartuserid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT cart_username_fkey FOREIGN KEY (cartusername)
        REFERENCES public.users (username) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cart
    OWNER to postgres;
	
-- Table: public.cartmenuitem

-- DROP TABLE IF EXISTS public.cartmenuitem;

CREATE TABLE IF NOT EXISTS public.cartmenuitem
(
    cartmenuitemid integer NOT NULL DEFAULT nextval('cartitem_id_seq'::regclass),
    cartid integer NOT NULL,
    menuitemid integer NOT NULL,
    canteenid integer NOT NULL,
    menuitemquantity integer NOT NULL,
    permenuitemprice integer NOT NULL,
    totalmenuitemprice integer NOT NULL,
    createddate time without time zone,
    updateddate time without time zone,
    CONSTRAINT cartmenuitem_pkey PRIMARY KEY (cartmenuitemid),
    CONSTRAINT cart_canteen_fkey FOREIGN KEY (canteenid)
        REFERENCES public.canteen (canteenid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT cart_menu_fkey FOREIGN KEY (cartid)
        REFERENCES public.cart (cartid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cart_menuitem_fkey FOREIGN KEY (menuitemid)
        REFERENCES public.cartmenuitem (cartmenuitemid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cartmenuitem
    OWNER to postgres;
-- Table: public.feedback

-- DROP TABLE IF EXISTS public.feedback;

CREATE TABLE IF NOT EXISTS public.feedback
(
    feedbackid integer NOT NULL,
    feedbackuserid integer NOT NULL,
    feedbackdesc character varying(120) COLLATE pg_catalog."default" NOT NULL,
    orderid integer NOT NULL,
    menuitemid integer NOT NULL,
    feedbackdate time without time zone NOT NULL,
    feedbackstatus character varying(50) COLLATE pg_catalog."default" NOT NULL,
    feedbackaction character varying(120) COLLATE pg_catalog."default",
    feedbackclosureremarks character varying(120) COLLATE pg_catalog."default",
    feedbackactionuserid character varying(120) COLLATE pg_catalog."default",
    createddate time without time zone,
    updateddate time without time zone,
    feedbackusername character varying(120) COLLATE pg_catalog."default",
    CONSTRAINT feedback_pkey PRIMARY KEY (feedbackid),
    CONSTRAINT feedback_menuitem_fkey FOREIGN KEY (menuitemid)
        REFERENCES public.menuitem (menuitemid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT feedback_order_fkey FOREIGN KEY (orderid)
        REFERENCES public."order" (orderid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT feedback_user_fkey FOREIGN KEY (feedbackusername)
        REFERENCES public.users (username) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT feedback_userid_fkey FOREIGN KEY (feedbackuserid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.feedback
    OWNER to postgres;
-- Table: public.menuitem

-- DROP TABLE IF EXISTS public.menuitem;

CREATE TABLE IF NOT EXISTS public.menuitem
(
    menuitemid integer NOT NULL DEFAULT nextval('menuitem_id_seq'::regclass),
    canteenid integer NOT NULL,
    menuitemdesc character varying(120) COLLATE pg_catalog."default" NOT NULL,
    "Permenuitemprice" integer NOT NULL,
    menuitemstatus character varying(50) COLLATE pg_catalog."default" NOT NULL,
    menuitemtype character varying(50) COLLATE pg_catalog."default" NOT NULL,
    createddate time without time zone,
    updateddate time without time zone,
    CONSTRAINT menuitem_pkey PRIMARY KEY (menuitemid),
    CONSTRAINT canteen_menuitem_cart_fkey FOREIGN KEY (canteenid)
        REFERENCES public.canteen (canteenid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.menuitem
    OWNER to postgres;
-- Table: public.notification

-- DROP TABLE IF EXISTS public.notification;

CREATE TABLE IF NOT EXISTS public.notification
(
    notificationid integer NOT NULL DEFAULT nextval('notification_id_seq'::regclass),
    userid integer NOT NULL,
    notificationdesc character varying(120) COLLATE pg_catalog."default" NOT NULL,
    notificationcreateddate time without time zone NOT NULL,
    notificationtype character varying(120) COLLATE pg_catalog."default" NOT NULL,
    notificationstatus character varying(50) COLLATE pg_catalog."default" NOT NULL,
    createddate time without time zone,
    updateddate time without time zone,
    CONSTRAINT notification_pkey PRIMARY KEY (notificationid),
    CONSTRAINT notification_user_fkey FOREIGN KEY (userid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.notification
    OWNER to postgres;

-- Table: public.order

-- DROP TABLE IF EXISTS public."order";

CREATE TABLE IF NOT EXISTS public."order"
(
    orderid integer NOT NULL DEFAULT nextval('order_id_seq'::regclass),
    userid character varying(120) COLLATE pg_catalog."default" NOT NULL,
    orderdate time without time zone NOT NULL,
    cartid integer NOT NULL,
    orderstatus character varying(120) COLLATE pg_catalog."default" NOT NULL,
    paymentid integer NOT NULL,
    orderprice integer NOT NULL,
    createdon time without time zone,
    updatedon time without time zone,
    CONSTRAINT orderid_pkey PRIMARY KEY (orderid),
    CONSTRAINT order_cart_fkey FOREIGN KEY (cartid)
        REFERENCES public.cart (cartid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."order"
    OWNER to postgres;
-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    userid integer NOT NULL DEFAULT nextval('users_userid_seq'::regclass),
    username character varying(80) COLLATE pg_catalog."default" NOT NULL,
    firstname character varying(120) COLLATE pg_catalog."default" NOT NULL,
    lastname character varying(120) COLLATE pg_catalog."default" NOT NULL,
    mobileno bigint NOT NULL,
    email character varying(120) COLLATE pg_catalog."default" NOT NULL,
    aadharid character varying(120) COLLATE pg_catalog."default" NOT NULL,
    userrole user_userrole,
    userstatus user_userstatus,
    password character varying(100) COLLATE pg_catalog."default" NOT NULL,
    registered_on timestamp without time zone NOT NULL,
    updateddate timestamp without time zone NOT NULL,
    remarks character varying(120) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (userid),
    CONSTRAINT user_id UNIQUE (userid)
        INCLUDE(userid),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT users_name UNIQUE (username)
        INCLUDE(username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

COMMENT ON CONSTRAINT users_name ON public.users
    IS 'user name should be unique';
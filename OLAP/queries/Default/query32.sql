-- start query 32 in stream 0 using template query32.tpl
select top 100 sum(cs_ext_discount_amt)  as "excess discount amount" 
from 
   catalog_sales 
   ,item 
   ,date_dim
where
i_manufact_id = 471
and i_item_sk = cs_item_sk 
and d_date between '2001-01-28' and 
        (cast('2001-01-28' as date) + 90 days)
and d_date_sk = cs_sold_date_sk 
and cs_ext_discount_amt  
     > ( 
         select 
            1.3 * avg(cs_ext_discount_amt) 
         from 
            catalog_sales 
           ,date_dim
         where 
              cs_item_sk = i_item_sk 
          and d_date between '2001-01-28' and
                             (cast('2001-01-28' as date) + 90 days)
          and d_date_sk = cs_sold_date_sk 
      ) 
;
-- end query 32 in stream 0 using template query32.tpl

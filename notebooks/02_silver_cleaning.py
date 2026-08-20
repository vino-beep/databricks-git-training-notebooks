# Databricks notebook source 

bronze_df = spark.table( 

   "data_engineering.bronze.customers" 

) 

silver_df = ( 

   bronze_df 

   .dropDuplicates(["customer_id"]) 

   .dropna(subset=["customer_id"]) 

) 
print("this is silver dataframe")
display(silver_df) 
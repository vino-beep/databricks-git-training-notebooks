# Databricks notebook source 

 

# Bronze Layer - Raw Data Ingestion 

 

file_path = "/Volumes/data_engineering/customer/raw/customers.csv" 

 

df = spark.read.csv( 

   file_path, 

   header=True, 

   inferSchema=True 

) 

 

display(df) 
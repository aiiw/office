```sql
update product_info t 
set (t.salename,t.xsqy)
=(select c.salename,c.xsqy from contract_erp c  where c.contractcode=t.contractid)
where t.contractid in(select c.contractcode from contract_erp c) and t.contractid is not null and t.salename is null;
```


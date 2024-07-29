```
BEGIN
  FOR rec IN (
    SELECT t.sfaadocno, 
           getbatchnum123(t.sfaadocno) AS result
      FROM sfaa_t t
     WHERE t.sfaadocno <> 'X'
  ) LOOP
    DBMS_OUTPUT.PUT_LINE('sfaadocno: ' || rec.sfaadocno || ', result: ' || rec.result);
  END LOOP;
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Error occurred: ' || SQLERRM);
END;
```


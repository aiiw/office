$ {
    if (len(no2) = 0, "",
        if (find("*", no2) > 0, "AND t.xmda033 LIKE '%" + replace(no2, "*", "%") + "%'", "AND t.xmda033='" + no2 + "'"))
}
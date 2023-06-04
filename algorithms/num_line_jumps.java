String response = "NO";
boolean canCatchUp = (v2 < v1);
if(canCatchUp) {
    boolean willIntersectOnLand = (x1 - x2) % (v2 - v1) == 0;
    if(willIntersectOnLand) {
        response = "YES";
    }
}

System.out.println(response);

% تعریف موقعیت‌ها
:- dynamic rover/2.
:- dynamic goal/2.
:- dynamic obstacle/2.

% جهت‌های حرکت
direction(-1, 0).  
direction(1, 0).   
direction(0, -1).  
direction(0, 1).   

% بررسی معتبر بودن موقعیت
is_valid(X, Y) :-
    X >= 0, X < 12,
    Y >= 0, Y < 16,
    \+ obstacle(X, Y).

% BFS برای یافتن **کوتاه‌ترین مسیر**
bfs([[X, Y, Path] | _], _, Path) :-
    goal(X, Y), !.

bfs([[X, Y, Path] | Rest], Visited, ShortestPath) :-
    findall([NX, NY, [[NX, NY] | Path]],
            (direction(DX, DY), NX is X + DX, NY is Y + DY, 
             is_valid(NX, NY), \+ member([NX, NY], Visited)),
            Neighbors),
    append(Rest, Neighbors, NewQueue),
    append(Visited, Neighbors, NewVisited),
    bfs(NewQueue, NewVisited, ShortestPath).

% اجرای الگوریتم برای یافتن مسیر
find_path(OptimizedPath) :-
    rover(RX, RY),
    bfs([[RX, RY, [[RX, RY]]]], [[RX, RY]], FullPath),
    reverse(FullPath, OptimizedPath).

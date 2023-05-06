#include <bits/stdc++.h>

#define ll long long
#define sz(a) (int)a.size()
#define fu(i,a,b) for(int i=a;i<=b;++i)
#define fd(i,a,b) for(int i=a;i>=b;--i)

using namespace std;

const int N = 100003;

int n, m, a[N];
int res;

bool check (int rad)
{
    rad *= 2;
    int pre = a[1];
    int use = 1;
    fu(i,1,n)
        if (a[i] - pre > rad)
        {
            pre = a[i];
            use++;
        }
    return use <= m;
}

int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) cin >> a[i];
    sort(a+1,a+n+1);
    for (int d = 1; d <= 2500; ++d)
        if (check(d))
        {
            cout << d;
            break;
        }
    return 0;
}

#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define sz(a) (int)a.size()
#define fu(i,a,b) for(int i=a;i<=b;++i)
#define fd(i,a,b) for(int i=a;i>=b;--i)

using namespace std;


const ll oo = 2e18;
const int N = 10;
const int M = 1000003;
const ll mod = 1e9 + 7;
typedef pair<ll, ll> ii;

int n = 9;
int t[N], c[N];
vector <int> a[N], color;
ll res = oo;

int Map(char x)
{
    if (x == 'D') return 0;
    if (x == 'X') return 1;
    return 2;
}

void update()
{
    vector <int> temp;
    temp = color;
    ll cost = 0;
    fu(i,1,n)
        if (c[i])
        {
            cost += t[i] * c[i];
            for (auto j : a[i])
            {
                temp[j] += c[i];
                temp[j] %= 3;
            }
        }
    bool ok = true;
    fu(i,1,n)
        if (temp[i] != 1) ok = false;

    if (ok) res = min(res, cost);

}

void solve(int pos)
{
    if (pos == 10)
    {
        update();
        return;
    }

    for (int i = 0; i <= 2; ++i)
    {
        c[pos] = i;
        solve(pos + 1);
    }
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    fu(i,1,n)
    {
        cin >> t[i];
        string inp;
        cin >> inp;
        fu(j, 0, sz(inp) - 1)
            a[i].pb(inp[j] - '0');
    }
    string inp;
    cin >> inp;
    color.resize(N);
    fu(i, 0, sz(inp) - 1) color[i + 1] = Map(inp[i]);
    solve(1);
    cout << (res == oo ? -1 : res);
    return 0;
}

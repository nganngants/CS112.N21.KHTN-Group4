#include<bits/stdc++.h>
#define maxn 100001
#define ll long long
#define mod (ll)(1e9+7)
using namespace std;

vector<int> a[maxn];
ll n,m,x,y,cnt,res;
bool vs[maxn];

void dfs(int u)
{
    if(vs[u] == 1)return ;
    cnt++;
    vs[u] = 1;
    for(auto v:a[u])
        dfs(v);
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
//    freopen("test.inp","r",stdin);
//    freopen("test.out","w",stdout);
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        cin>>x>>y;
        a[x].push_back(y);
        a[y].push_back(x);
    }
    for(int i=1;i<=n;i++)
        if(vs[i]==0)
        {
            dfs(i);
            res+= cnt*(n-cnt);
            cnt = 0;
        }
    cout<<res/2;
    return 0;
}

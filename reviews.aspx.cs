using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;

public partial class reviews : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string[] reviews = File.ReadAllLines(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\preview.txt");
        Label1.Text = reviews[1];
        Label2.Text = reviews[2];
        Label3.Text = reviews[3];
        Label4.Text = reviews[4];
        Label5.Text = reviews[6];
        Label6.Text = reviews[7];
        Label7.Text = reviews[8];
        Label8.Text = reviews[9];
        Label9.Text = reviews[10];
        
     }
}
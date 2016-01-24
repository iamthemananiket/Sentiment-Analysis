using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using IronPython;
using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using System.Diagnostics;
using System.IO;
using System.Web.UI.DataVisualization.Charting;
using System.Drawing;

public partial class SentimentAnalysis : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        name.Text = "";
    }
    protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
    {

    }
    protected void LinkButton2_Click(object sender, EventArgs e)
    {
        Response.Redirect("https://www.facebook.com/iamthemananiket");  /*Redirect to the respective pages*/
    }
    protected void LinkButton3_Click(object sender, EventArgs e)
    {
        Response.Redirect("https://www.facebook.com/ashishpatil04");
    }
    protected void LinkButton4_Click(object sender, EventArgs e)
    {
       
    }
protected void  LinkButton1_Click(object sender, EventArgs e)
{
    
}
protected void  LinkButton4_Click1(object sender, EventArgs e)
{
    Response.Redirect("https://www.facebook.com/ranjitashetty.ranjitashetty");
}
protected void TextBox1_TextChanged(object sender, EventArgs e)
{
 
    
}
protected void Button1_Click(object sender, EventArgs e)
{
    string contents = TextBox1.Text;            //Write Contents of TextBox into the playURL file
    File.WriteAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\playURL.txt", contents);
    dopython();                                 //Call the Python Nethod For processing
    string appname = File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\pappName.txt");
    name.Text = "Click link below for top rviews on  " + appname;
    
    string result = File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\presult.txt");

    final.Text = "Here is the Overall Sentiment for " + appname;
    score.Text = "The average rating for " + appname + " is";
    String scr = File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\score.txt");
    scores.Text = scr;

    if (String.Equals(result.ToString(), "negative"))       //Read the Result processed by the Python code
        Image1.ImageUrl = "thumbsdown.png";                 //Show the Thumbs Down image if result is negative
    else 
        Image1.ImageUrl = "Thumbs_Up.png";                  //Thumbs up if result is positive

}
protected void RadioButtonList1_SelectedIndexChanged1(object sender, EventArgs e)
{
    
    
}
protected void LinkButton2_Click1(object sender, EventArgs e)
{
    Response.Redirect("https://www.facebook.com/iamthemananiket");
}
protected void LinkButton1_Click1(object sender, EventArgs e)
{
    Response.Redirect("http://pes.edu/faculty/dr-shylaja-s-s");
}
protected void LinkButton3_Click1(object sender, EventArgs e)
{
    Response.Redirect("https://www.facebook.com/ashishpatil04");
}
protected void Button2_Click(object sender, EventArgs e)
{
    System.IO.File.WriteAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\prev.txt", string.Empty);
    Response.Redirect("SentimentAnalysis.aspx");
}
public static void dopython()
{
    
    Process p = new Process();                                  //Create a instance for Process class to hold the Python runtime
    p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
    p.StartInfo.FileName = @"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\fetch.py"; //Launch the Fetch file
    p.Start();
    p.WaitForExit();

    Process q = new Process();
    q.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
    q.StartInfo.FileName = @"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\logic.py";  //Launch the logic file
    q.Start();
    q.WaitForExit();
}
protected void RadioButtonList1_SelectedIndexChanged2(object sender, EventArgs e)
{
    like.Text = "Thanks for rating us  " + RadioButtonList1.SelectedValue;      //Accept the ratings
}
protected void Chart1_Load(object sender, EventArgs e)
{
    
}
protected void Button3_Click(object sender, EventArgs e)
{
    Random rnd = new Random();
    int s1 = Convert.ToInt32(File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\1s.txt")) + rnd.Next(500, 1000);
    int s2 = Convert.ToInt32(File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\2s.txt")) + rnd.Next(1000,1200);
    int s3 = Convert.ToInt32(File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\3s.txt")) + rnd.Next(1700,2100);
    int s4 = Convert.ToInt32(File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\4s.txt")) + rnd.Next(2200,2800);
    int s5 = Convert.ToInt32(File.ReadAllText(@"C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\5s.txt")) + rnd.Next(2200,2700);
    String[] x = { "1 Star", "2 Star", "3 Star", "4 star", "5 star" };
    int[] y = { s1, s2, s3, s4, s5 };
    Chart1.Series["Series1"].Points.DataBindXY(x, y);       //Designing the layout of the Bar Chart
    Chart1.Series["Series1"].Points[0].Color = Color.Yellow;
    Chart1.Series["Series1"].Points[1].Color = Color.Blue;
    Chart1.Series["Series1"].Points[2].Color = Color.Red;
    Chart1.Series["Series1"].Points[3].Color = Color.Green;
    Chart1.Series["Series1"].Points[4].Color = Color.Orange;
    Chart1.Series["Series1"].ChartType = SeriesChartType.Bar;
}
protected void rev_Click(object sender, EventArgs e)
{
    Response.Redirect("reviews.aspx");          //Redirect to page containing the reviews
}
}
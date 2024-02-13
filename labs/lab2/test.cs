using System;
using System.Drawing;
using System.Windows.Forms;
 
namespace Bransli
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
 
        private Graphics g;
        private Pen p;
 
        private void FirstLine(int x, int y, double a, double b)
        {
            g.DrawLine(p, x, y, (int)Math.Round(x + a * Math.Cos(b)), (int)Math.Round(y - a * Math.Sin(b)));
        }
 
        private void Draw(int x, int y, double a, double b)
        {
            if (a > 1)
            {
                FirstLine(x, y, a, b);
                x = (int)Math.Round(x + a * Math.Cos(b));
                y = (int)Math.Round(y - a * Math.Sin(b));
                Draw(x, y, a * 0.4, b - 14 * Math.PI / 30);
                Draw(x, y, a * 0.4, b + 14 * Math.PI / 30);
                Draw(x, y, a * 0.7, b + Math.PI / 30);
            }
        }
 
        private void button1_Click(object sender, EventArgs e)
        {
            g = picture_box.CreateGraphics();
            p = new Pen(Color.Black);
            g.FillRectangle(Brushes.White, 0, 0, picture_box.Width, picture_box.Height);
            Draw(240, 350, 100, Math.PI / 2);
        }
    }
}
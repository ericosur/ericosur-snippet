using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace cstest1
{
    class Program
    {
        static void Main(string[] args)
        {
            Prob26();
            Problem26();
        }

        // brute force for problem #26 http://projecteuler.net/problem=26
        static void Prob26()
        {
            DateTime start = DateTime.Now;
            int max = 0;
            int maxd = 0;
            for (int d = 2; d < 1000; ++d)
            {
                var reminders = new HashSet<int>();
                int x = 1;
                int len = 0;
                while (x < d)
                    x *= 10;

                while (x != 0)
                {
                    if (reminders.Contains(x))
                        break;

                    reminders.Add(x);

                    while (x < d)
                    {
                        x *= 10;
                        len++;
                    }
                    x = x % d;
                }
                if (x != 0)
                {
                    if (len > max)
                    {
                        maxd = d;
                        max = len;
                    }
                }
            }
            Console.WriteLine(maxd);
            Console.WriteLine((DateTime.Now - start).TotalMilliseconds + " ms");
        }

        // using the method for cycle detection
        // http://en.wikipedia.org/wiki/Cycle_detection
        static void Problem26()
        {
            DateTime start = DateTime.Now;
            int numLongestRecurring = 1;
            int cycle = 0;
            for (int i = 1; i < 1000; i++)
            {
                int power = 1, lam = 1;
                int tortoise = 1 / i;
                int tortoiseRem = (1 % i) * 10;
                int hare = tortoiseRem / i;
                int hareRem = (tortoiseRem % i) * 10;
                while (tortoise != hare || tortoiseRem != hareRem)
                {
                    if (power == lam)
                    {
                        tortoise = hare;
                        tortoiseRem = hareRem;
                        power *= 2;
                        lam = 0;
                    }
                    hare = hareRem / i;
                    hareRem = (hareRem % i) * 10;
                    lam++;
                }
                if (lam > cycle)
                {
                    cycle = lam;
                    numLongestRecurring = i;
                }
            }
            Console.WriteLine("Number with longest recurring cycle: {0}\nCycle Length: {1}", numLongestRecurring, cycle);
            Console.WriteLine((DateTime.Now - start).TotalMilliseconds + " ms");
            //Console.ReadLine();
        }    
    }
}

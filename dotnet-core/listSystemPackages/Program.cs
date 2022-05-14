using System;
using System.IO;
using System.Xml;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace openrmfpro_msg_score
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = args[0] + "/api/external/systempackages/?applicationKey=" + args[1];
            HttpClient HttpClient = HttpClientFactory.Create();
            // Setting the Content-type to application/json
            HttpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            // Setting the Token Header and the Root Token
            HttpClient.DefaultRequestHeaders.Add("Authorization", "Bearer " + args[2]);

            var result = HttpClient.GetStringAsync(url).GetAwaiter().GetResult();

            HttpClient.Dispose();
            Console.WriteLine(result);
        }
    }
}
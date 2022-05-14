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
            string url = args[0] + "/api/external/testauthentication";
            HttpClient HttpClient = HttpClientFactory.Create();
            // Setting the Content-type to application/json
            HttpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            // Setting the Token Header and the Root Token
            HttpClient.DefaultRequestHeaders.Add("Authorization", "Bearer " + args[2]);
            MultipartFormDataContent formData = new MultipartFormDataContent();
            formData.Add(new StringContent(System.Web.HttpUtility.HtmlEncode(args[1])), "applicationKey");

            var req = new HttpRequestMessage(HttpMethod.Post, url) { Content = formData};
            var res = HttpClient.SendAsync(req).GetAwaiter().GetResult();

            HttpClient.Dispose();
            Console.WriteLine("Success = " + res.IsSuccessStatusCode);
            Console.WriteLine("Status = " + res.StatusCode);

        }
    }
}
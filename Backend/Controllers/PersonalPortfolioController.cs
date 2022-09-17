using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Backend.Data;
using System.IO;

namespace Backend.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PersonalPortfolioController : ControllerBase
    {
        private readonly ILogger<PersonalPortfolioController> _logger;

        public PersonalPortfolioController(ILogger<PersonalPortfolioController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Clothing> Get()
        {
            var clothingList = new List<Clothing>();

            return clothingList;
        }

        [HttpPut]
        public void Put(Image image)
        {
            Console.WriteLine(image.Encoded);

            // Categorize the image
            // Put the image in the db as categorized
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Backend.Data;

namespace Backend.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class RandomPortfolioController : ControllerBase
    {
        private readonly ILogger<RandomPortfolioController> _logger;

        private IClothingFactory _clothingFactory;

        public RandomPortfolioController(ILogger<RandomPortfolioController> logger)
        {
            _logger = logger;
            _clothingFactory = new RandomClothingFactory();
        }

        [HttpGet]
        public IEnumerable<Clothing> Get()
        {
            var clothingList = new List<Clothing>();

            for (int i = 0; i < 5; i++)
            {
                clothingList.Add(_clothingFactory.CreateClothing());
            }

            return clothingList;
        }
    }
}

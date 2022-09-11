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

        private IClothingFactory clothingFactory;

        public RandomPortfolioController(ILogger<RandomPortfolioController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Clothing> Get()
        {
            return null;
        }
    }
}

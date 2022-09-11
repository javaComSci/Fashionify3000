using System;

namespace Backend.Data
{
    public class RandomClothingFactory : IClothingFactory
    {
        public RandomClothingFactory()
        {
        }

        public Clothing CreateClothing()
        {
            Random rnd = new Random();
            var rndVal = rnd.Next(1, 3);

            Clothing piece = rndVal == 1 ? new Bottom() : new Top();
            piece.Attribute = "pink";
            return piece;
        }
    }
}

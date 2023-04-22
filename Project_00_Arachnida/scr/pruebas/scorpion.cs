using System;
using System.IO;
using MetadataExtractor;

class Program
{
    static void Main(string[] args)
    {
        string imagePath = "ruta/a/la/imagen.jpg";
        IEnumerable<MetadataExtractor.Directory> directories = ImageMetadataReader.ReadMetadata(imagePath);
        foreach (var directory in directories)
        {
            foreach (var tag in directory.Tags)
            {
                Console.WriteLine($"{directory.Name} - {tag.Name} = {tag.Description}");
            }
            if (directory.HasError)
            {
                foreach (var error in directory.Errors)
                    Console.WriteLine($"ERROR: {error}");
            }
        }
    }
}
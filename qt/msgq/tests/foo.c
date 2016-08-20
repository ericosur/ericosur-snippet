#include <stdio.h>
#include <stdlib.h>
#include <libconfig.h>

/* This example reads the configuration file 'example.cfg' and displays
 * some of its contents.
 */
#define CFGNAME "foo.cfg"

int main(int argc, char **argv)
{
  config_t cfg;
  config_setting_t *setting;
  const char *str;

  config_init(&cfg);

  /* Read the file. If there is an error, report it and exit. */
  if(! config_read_file(&cfg, CFGNAME))
  {
    fprintf(stderr, "%s:%d - %s\n", config_error_file(&cfg),
            config_error_line(&cfg), config_error_text(&cfg));
    config_destroy(&cfg);
    return(EXIT_FAILURE);
  }

  /* Get the store name. */
  if(config_lookup_string(&cfg, "version", &str))
    printf("version: %s\n", str);
  else
    fprintf(stderr, "No 'version' setting in configuration file.\n");

  /* Output a list of all books in the inventory. */
  setting = config_lookup(&cfg, "application");
  if(setting != NULL)
  {
    int count = config_setting_length(setting);

    printf("%-15s\t%s\n", "name", "key");
    for(int i = 0; i < count; ++i)
    {
      config_setting_t *apps = config_setting_get_elem(setting, i);

      /* Only output the record if all of the expected fields are present. */
      const char *name;
      int key;

      if (!(config_setting_lookup_string(apps, "name", &name)
           && config_setting_lookup_int(apps, "key", &key)))
        continue;

      printf("%-15s\t0x%08X\n", name, key);
    }
    printf("\n");
  }


  config_destroy(&cfg);
  return(EXIT_SUCCESS);
}

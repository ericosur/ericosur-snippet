#include <stdio.h>
#include <string.h>
#include <stdarg.h>

/* Composes a string accordingly to format with correctly escaping JSON literals.
 * Correctly fails when runs up of output buffer space.
 * Replaces all occurences of ' with " in format string for convenience.
 * Terminates a string with '\0'.
 * Format specifiers:
 *    %% - literally '%'
 *    %d - integer
 *    %s - string
 *    %b - boolean
 *    '  - "
 * Returns: number of written bytes on success, negative value on fail
 */

static char lookup_escape_code(char c);
static int json_escape(char *out, char *in, int in_len);

int jvsnprintf(char *out, size_t n, const char *format, va_list ap);

int jsnprintf(char *out, size_t n, const char *format, ...)
{
   va_list ap;
   va_start(ap, format);
   int ret = jvsnprintf(out, n, format, ap);
   va_end(ap);
   return ret;
}

int jvsnprintf(char *out, size_t n, const char *format, va_list ap)
{
   memset(out, 0, n);

   int ret = 0;

   int i;
   for(i = 0; i < strlen(format); i++)
   {
      char *tail = &out[strlen(out)];
      int remains = n - strlen(out);

      if(format[i] == '\'')
      {
         *tail = '"';
         ret++;
      }
      else if(format[i] == '%')
      {
         char *str;
         int bytes_written;

         switch(format[i+1])
         {
            case '%':
               if(remains < 2) return -1;
               *tail = '%';
               ret++;
               break;
            case 'd':
               bytes_written = snprintf(tail, remains-1, "%d", va_arg(ap, int));
               if(bytes_written < 0 || bytes_written > remains-1) return -1;
               ret += bytes_written;
               break;
            case 's':
               str = va_arg(ap, char *);
               if(remains < strlen(str) * 6 + 2 + 1) return -1;

               strcat(tail, "\"");
               bytes_written = json_escape(&tail[1], str, strlen(str));
               strcat(tail, "\"");
               ret += bytes_written + 2;
               break;
            case 'b':
               if(remains < strlen("false") + 1) return -1;
               char *end = strcat(tail, va_arg(ap, int) ? "true" : "false");
               ret += end - tail;
               break;
            default:
               return -1;
         }
         i++;
      }
      else
      {
         *tail = format[i];
         ret++;
      }
   }

   return ret;
}

char popular_chars[][2] = {
   {'\x22', '"'},
   {'\x5c', '\\'},
   {'\x2f', '/'},
   {'\x08', 'b'},
   {'\x0c', 'f'},
   {'\x0a', 'n'},
   {'\x0d', 'r'},
   {'\x09', 't'},
   { '\0' },
};

static char lookup_escape_code(char c)
{
   int i = 0;

   for(i = 0; popular_chars[i][0]; i++)
   {
      if(popular_chars[i][0] == c)
         return popular_chars[i][1];
   }

   return '\0';
}

static int json_escape(char *out, char *in, int in_len)
{
   // Escape string accordingly to IETF RFC4627

   int bytes_written = 0;

   memset(out, 0, in_len * 6);

   int i;
   for(i = 0; i < in_len; i++)
   {
      char *tail = &out[strlen(out)];

      if(lookup_escape_code(in[i]))
      {
         sprintf(tail, "%c%c", '\\', lookup_escape_code(in[i]));
         bytes_written += 2;
      }
      // else if(in[i] & (1 << 7))
      // {
      //    sprintf(tail, "\\u00%02x", (unsigned char) in[i]);
      //    bytes_written += 6;
      // }
      else
      {
         *tail = in[i];
         bytes_written += 1;
      }
   }

   return bytes_written;
}

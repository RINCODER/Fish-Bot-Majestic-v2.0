using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using System.Threading;
using System.Windows.Controls;
using System.Drawing;

namespace FISHBOT.Spasibo
{
    internal class Bot
    {
        #region variables
        private static bool botWork = false; //загулшка на нажатие клавиши
        private static int counter = 0; //счетчик
        #endregion



            public async static void GetStart()
            {
            while (true)
            {
                if (Keyboard.IsKeyDown(Key.O))
                {
                    botWork = true;
                    MessageBox.Show($"botWork: {botWork}");
                }

                else if (Keyboard.IsKeyDown(Key.P))
                {
                    botWork = false;
                    MessageBox.Show($"botWork: {botWork}");
                }

                if (botWork  && counter == 0)
                {
                    MessageBox.Show($"start: {botWork}");
                    //Thread threadCheckTrables = new Thread(CheckTrables);
                    Thread threadCastFishingRod = new Thread(CastFishingRod);
                    threadCastFishingRod.Start();
                    counter++;
                }
                await Task.Delay(120);
            }
        }




        private static void CheckTrables() //поиск проблемм (предложения по типу взять на руки, информация о голоде и воде, наживке)
        {

        }

        private static bool CheckError(string name)
        {
            //проверка на то была ли закинута удочка
            //проверка на срыв рыбы
            //проверка на выловленую рыбу
            return true;
        }

        private static void CastFishingRod() //закидывание удочки
        {
            while (botWork)
            {
                Thread.Sleep(5);
            }
            MessageBox.Show("Закинул");
            Thread threadFishing = new Thread(Fishing);
            threadFishing.Start();
        }

        private static void Fishing() //рыбачество
        {
            while (botWork)
            {

            }
            MessageBox.Show("по рыбачи");
            Thread threadPullFish = new Thread(PullFish);
            threadPullFish.Start();
        }

        private static void PullFish() //вытаскивание рыбы
        {
            MessageBox.Show("вытащил");
            counter = 0;
        }



    }
}

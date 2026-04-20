using HarmonyLib;
using View.Handlers;

namespace TerraNilAP;

[HarmonyPatch(typeof(ProgressionInterfaceHandler), "OpenHandbookToCurrentMissionPage")]
class ProgressionInterfaceHandlerPatch
{
    public static bool Prefix(object[] __args)
    {
        var action = __args[1] as System.Action;
        if (action != null) action();
        return false;
    }
}

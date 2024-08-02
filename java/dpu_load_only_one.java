
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.file.Path;

import com.upmem.dpu.Dpu;
import com.upmem.dpu.DpuException;
import com.upmem.dpu.DpuSystem;

public class dpu_load_only_one {

  public static void main(String[] args) throws DpuException {
    //try(DpuSystem system = DpuSystem.allocate(DpuSystem.ALLOCATE_ALL, "")) {
    try(DpuSystem system = DpuSystem.allocateRanks(1, "")) {

    Dpu dpu = system.dpus().get(0);

    for (int i = 0; i < 1000000; i++) {
      dpu.load("/tmp/afterSwResetIram7061056236090871404.iram");
    }
            }
        }
    }

import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { environment } from '../../.environment/environment.local'
import { Observable } from 'rxjs'
import { Solucion } from 'src/models/solucion'

@Injectable({
  providedIn: 'root'
})
export class ArchivosService {

  private server: string = environment.server

  constructor(private http: HttpClient) { }

  subirArchivo(file: File): Observable<any> {
    const formData = new FormData()
    formData.append('file', file, file.name)

    return this.http.post(`${this.server}/upload`, formData, {
      reportProgress: true,
      observe: 'events'
    })
  }

  descargarArchivo(filename: string): Observable<Blob> {
    // Usar el endpoint '/download/{filename}' para descargar archivos
    return this.http.get(
      `${this.server}/download/${filename}`,
      { responseType: 'blob' }
    )
  }

  calcularSolucion(digit: string): Observable<Solucion> {
    return this.http.get<Solucion>(`${this.server}/resolver/${digit}`);
  }
}
